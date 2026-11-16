---
title: "Flasher les appareils Rayhunter : guide complet"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Flashez et configurez Rayhunter pour détecter les IMSI-catchers. Vérifiez les appareils pris en charge, installez le micrologiciel, contrôlez le fonctionnement et résolvez les problèmes courants."
tags: ["Rayhunter", "IMSI-catcher", "simulateur de station cellulaire", "sécurité mobile", "détection de surveillance", "protection de la vie privée", "Orbic RC400L", "TP-Link M7350", "point d'accès mobile", "flashage d'appareil", "cybersécurité", "sécurité sans fil", "contre-mesures à la surveillance", "EFF", "outils de confidentialité", "acheter Rayhunter", "guide d'installation", "configuration", "appareils pris en charge", "sécurité réseau"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Un appareil Rayhunter détecte des signaux sans fil et des IMSI-catchers, entourés de boucliers de sécurité"
coverCaption: "Système Rayhunter de détection des IMSI-catchers, pour protéger les communications mobiles de la surveillance"
---

**Guide complet pour flasher et configurer Rayhunter, le système de détection des IMSI-catchers.**

## En bref

**Rayhunter** est un système open source de détection des IMSI-catchers qui fonctionne sur des points d'accès mobiles modifiés. Il vous avertit lorsque des équipements de surveillance tentent d'intercepter des communications cellulaires. Ce guide couvre l'installation complète sur les appareils Orbic RC400L et TP-Link M7350, les options de configuration, l'analyse des menaces et l'efficacité sur les réseaux 5G. Il faut un appareil compatible équipé d'un modem Qualcomm. Le système détecte la surveillance sur les réseaux 2G, 3G et 4G grâce à plusieurs heuristiques. Il reste utile malgré l'adoption de la 5G, car les attaques qui forcent le retour vers des générations de réseau antérieures restent possibles. Il protège les journalistes, les militants et les personnes soucieuses de leur vie privée contre la surveillance gouvernementale, criminelle et commerciale.

**Rayhunter** est un outil open source conçu pour détecter les IMSI-catchers, ou simulateurs de stations cellulaires, capables d'intercepter des communications mobiles. Si vous cherchez à **acheter Rayhunter** ou souhaitez apprendre à flasher et configurer ces appareils, ce guide complet explique l'installation, la configuration et l'utilisation de **Rayhunter**.

**Déclaration de sponsoring :** Cet article est sponsorisé par [STS Collective](https://stscollective.com), le principal fournisseur d'appareils compatibles avec Rayhunter. Malgré ce sponsoring, toutes les informations techniques, analyses et recommandations de ce guide reposent uniquement sur la documentation officielle de Rayhunter, les retours de la communauté et une évaluation technique objective.

> 💰 **Remise exclusive pour les lecteurs :** Économisez jusqu'à 20 % sur les appareils Rayhunter et les produits STS Collective. Utilisez le code **SIMEONONSECURITY** au paiement ou [achetez directement avec la remise appliquée](https://stscollective.com/discount/SIMEONONSECURITY).

## Présentation de Rayhunter

**Rayhunter** est un système avancé de détection des IMSI-catchers, développé par l'**Electronic Frontier Foundation (EFF)**, une grande organisation à but non lucratif qui défend les libertés civiles dans le monde numérique. Depuis 1990, l'EFF défend la vie privée numérique, la liberté d'expression et l'innovation par le contentieux stratégique, l'analyse des politiques, l'activisme de terrain et le développement technologique.

Cet outil fonctionne sur des points d'accès mobiles compatibles et surveille en permanence les réseaux cellulaires à la recherche d'activités suspectes susceptibles d'indiquer la présence de simulateurs de stations cellulaires ou de Stingrays utilisés à des fins de surveillance. **Rayhunter** reflète l'engagement de l'EFF à fournir des outils pratiques de protection de la vie privée aux personnes et aux organisations qui ont besoin de se protéger contre la surveillance.

Le système **Rayhunter** envoie des alertes en temps réel lorsqu'il détecte un comportement potentiellement malveillant sur le réseau cellulaire. C'est un outil important pour les journalistes, les militants, les professionnels de la sécurité et les personnes soucieuses de leur vie privée. Des appareils compatibles **[avec Rayhunter](https://stscollective.com/collections/rayhunter)** sont disponibles auprès de STS Collective, le principal fournisseur de ces appareils spécialisés.

### Soutenir le projet Rayhunter

**Rayhunter** est un projet open source qui bénéficie du soutien de la communauté. Vous pouvez contribuer à son développement de plusieurs façons :

- **Acheter auprès de STS Collective** : STS Collective reverse une partie des bénéfices de chaque appareil Rayhunter vendu à l'EFF afin de soutenir le développement de **Rayhunter** et la recherche sur la vie privée.
- **Faire un don directement** : soutenez les actions de l'EFF en faveur de la vie privée et le développement de **Rayhunter** à l'adresse **[Faire un don à l’EFF](https://supporters.eff.org/donate/donate)**.
- **Participer à la communauté** : contribuez aux discussions, à la documentation et aux tests dans le dépôt GitHub officiel.

Votre soutien aide à maintenir **Rayhunter** gratuit, open source et en constante amélioration face aux nouvelles menaces de surveillance.

## Assistance, retours et communauté

**Rayhunter** bénéficie du soutien d'une communauté active de chercheurs en sécurité, de défenseurs de la vie privée et de citoyens concernés. Plusieurs canaux permettent d'obtenir de l'aide et de contribuer au projet :

- **Documentation officielle** : [Documentation Rayhunter](https://efforg.github.io/rayhunter/introduction.html), avec des guides complets d'installation, de configuration et d'utilisation
- **Dépôt GitHub** : [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Discussions de la communauté** : ouvrez des discussions sur GitHub concernant la compatibilité des appareils et le dépannage
- **Recherche en sécurité** : collaborez avec les chercheurs pour améliorer les capacités de détection de **Rayhunter**

Des appareils compatibles **[avec Rayhunter](https://stscollective.com/collections/rayhunter)** sont disponibles auprès de STS Collective.

## Questions fréquentes

### Faut-il une carte SIM active pour utiliser Rayhunter ?

**Rayhunter** nécessite une carte SIM dans l'appareil, mais celle-ci n'a pas besoin d'un forfait actif. Elle permet à l'appareil de se connecter aux réseaux cellulaires et de surveiller les activités suspectes. Pour utiliser l'appareil comme point d'accès pendant l'exécution de **Rayhunter**, il faut un forfait actif.

### Comment vérifier que mon appareil Rayhunter fonctionne ?

Activez l'heuristique de test dans les paramètres de configuration de **Rayhunter**. L'appareil déclenchera alors une alerte chaque fois qu'il détectera une station cellulaire, ce qui vous permettra de vérifier le fonctionnement du système. Ce mode de test produit beaucoup d'alertes, désactivez-le donc après la vérification.

### Faut-il choisir un appareil verrouillé ou déverrouillé ?

Pour utiliser **Rayhunter**, les appareils déverrouillés sont généralement préférables, surtout si vous comptez utiliser des cartes SIM autres que Verizon. La plupart des appareils Orbic de marque Verizon sont en réalité déverrouillés, mais vérifiez la compatibilité avant l'achat. STS Collective propose des appareils compatibles vérifiés **[avec Rayhunter](https://stscollective.com/collections/rayhunter)**.

{{< stscollective-ad "rayhunter" >}}

## Guide d'installation

### Installer la dernière version

L'installation de **Rayhunter** a été testée sur macOS et Ubuntu 24.04. Si vous rencontrez des problèmes avec les versions précompilées, vous devrez peut-être installer le logiciel depuis les sources.

#### Prérequis

Avant d'installer **Rayhunter**, assurez-vous d'avoir un appareil compatible. Sur les appareils TP-Link, insérez une carte SD formatée en FAT pour stocker les enregistrements.

#### Téléchargement et configuration

1. **Téléchargez la dernière version** : récupérez le fichier `rayhunter-vX.X.X-PLATFORM.zip` adapté sur la page officielle des versions :
   - Linux x64 : `linux-x64`
   - Linux ARM64 : `linux-aarch64`
   - Linux ARM v7/v8 : `linux-armv7`
   - macOS Intel : `macos-intel`
   - macOS ARM (M1/M2) : `macos-arm`
   - Windows : `windows-x86_64`

2. **Extrayez l'archive et accédez au dossier** :
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Connectez l'appareil** : allumez-le et connectez-vous en WiFi ou par partage de connexion USB. Vous devriez pouvoir accéder à :
   - Appareils Orbic : `http://192.168.1.1`
   - Appareils TP-Link : `http://192.168.0.1`

#### Installation selon l'appareil

**Pour les appareils Orbic RC400L** (disponibles **[avec Rayhunter](https://stscollective.com)**) :

**Rayhunter** propose deux méthodes d'installation sur les appareils Orbic RC400L. La méthode WiFi est recommandée pour la plupart des utilisateurs, tandis que la méthode USB offre des fonctions de débogage supplémentaires.

**Installation par WiFi (recommandée)** :
```bash
# Les utilisateurs macOS doivent d'abord exécuter cette commande :
xattr -d com.apple.quarantine installer

# Pour Verizon RC400L (le mot de passe administrateur est le même que le mot de passe WiFi) :
./installer orbic --admin-password 'YourWiFiPassword'

# Pour Kajeet/Smartspot RC400L :
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Pour les appareils Moxee (format du mot de passe : 12$ + les 3 derniers chiffres du mot de passe WiFi) :
./installer orbic --admin-password='12$XXX'
```

**Installation par USB (utilisateurs avancés)** :
La méthode USB active l'accès ADB (Android Debug Bridge) pour le débogage avancé, mais n'est pas recommandée pour une installation classique :

```bash
# AVERTISSEMENT : l'installateur USB n'est pas recommandé dans la plupart des cas
./installer orbic-usb
```

Cette méthode force le passage de l'appareil en mode débogage pour activer ADB, installe rootshell et **Rayhunter**, puis redémarre l'appareil. Utilisez-la uniquement si vous avez besoin d'ADB pour d'autres tâches.

**Pour les appareils TP-Link M7350** (disponibles **[avec Rayhunter](https://stscollective.com)**) :
```bash
./installer tplink
```

L'installateur termine le flashage de **Rayhunter** et redémarre l'appareil. Une ligne verte à l'écran indique que **Rayhunter** fonctionne correctement.

### Installer depuis les sources

Pour les développeurs ou les utilisateurs qui doivent compiler **Rayhunter** depuis les sources, le projet comprend :

- **Interface** : application SvelteKit en JavaScript (`./daemon/web/`)
- **Serveur** : binaire Rust `rayhunter-daemon` (`./daemon/`)
- **Installateur** : binaire Rust qui regroupe tous les composants (`./installer`)

#### Dépendances de compilation

Installez les dépendances suivantes :
- Le langage de programmation Rust
- Node.js/npm
- Outils de compilation C (`build-essential` sous Linux, `xcode-select --install` sous macOS)

#### Compilation

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Remplacez 'orbic' par le type de votre appareil
```

Pour le développement de l'interface avec rechargement automatique :
```bash
cd daemon/web
npm run dev
# Ou avec une cible personnalisée :
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Mettre Rayhunter à jour

La mise à jour de **Rayhunter** suit la même procédure que l'installation. Répétez les étapes avec la dernière version pour utiliser la version la plus récente de **Rayhunter**.

## Configuration

Vous pouvez configurer **Rayhunter** depuis l'interface Web ou en modifiant directement `/data/rayhunter/config.toml` sur l'appareil.

### Configuration de l'interface Web

Pour ouvrir l'interface Web de **Rayhunter**, connectez-vous au réseau de l'appareil et visitez :
- Orbic : `http://192.168.1.1:8080`
- TP-Link : `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Tableau de bord de l'interface Web Rayhunter" caption="L'interface Web Rayhunter propose des options complètes de surveillance et de configuration" >}}

#### Principales options de configuration

**Niveau d'affichage de l'appareil** : définit ce que **Rayhunter** affiche à l'écran :
- **Mode invisible** : aucune information à l'écran
- **Mode discret** : indicateur sous forme de ligne colorée (verte = sûr, rouge = alerte, blanche = pause)
- **Mode démo** : affiche un orque avec une ligne d'état
- **Logo EFF** : affiche le logo EFF et une ligne d'état
- **Haute visibilité** : affichage couleur plein écran

**Mode des commandes de l'appareil** : configure le comportement du bouton d'alimentation :
- **Désactiver la commande par bouton** : le bouton d'alimentation est désactivé pour **Rayhunter**
- **Double appui pour redémarrer l'enregistrement** : réinitialise les alertes et relance la surveillance

**Paramètres de notification** : configurez l'URL ntfy pour les alertes à distance et activez ou désactivez les notifications d'avertissement et de batterie faible.

**Heuristiques d'analyse** : activez ou désactivez certains algorithmes de détection de **Rayhunter** selon votre environnement et votre modèle de menace.

## Désinstaller Rayhunter

### Appareils Orbic

Pour supprimer **Rayhunter** des appareils Orbic, exécutez :

```bash
./installer util orbic-shell --admin-password mypassword
```

Dans le shell de l'appareil :

> **Avertissement :** Les commandes suivantes suppriment définitivement les fichiers Rayhunter et ses scripts de démarrage. Vérifiez que vous êtes dans le shell de l'appareil prévu, sauvegardez les enregistrements ou la configuration nécessaires et gardez l'installateur et le micrologiciel compatible à portée de main. Ensuite, vérifiez que les fichiers ont disparu et que l'appareil redémarre sans le service Rayhunter. Pour revenir en arrière, réinstallez la version correspondante depuis le dépôt officiel.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### Appareils TP-Link

Pour désinstaller Rayhunter d'un appareil TP-Link :

> **Avertissement :** Ces commandes suppriment les fichiers Rayhunter et son script de démarrage de l'appareil TP-Link. Exportez d'abord les enregistrements et la configuration. Exécutez les commandes uniquement dans le shell de l'appareil, puis vérifiez que les chemins ont disparu et que l'appareil démarre normalement. Pour annuler l'opération, réinstallez la version correspondante depuis le dépôt officiel.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Supprimez les éventuels déclencheurs de port restants dans l'interface d'administration TP-Link, sous Settings > NAT Settings > Port Triggers.

## Utiliser Rayhunter

Après l'installation, **Rayhunter** démarre automatiquement et surveille en permanence les réseaux cellulaires à la recherche d'activités suspectes. En fonctionnement normal, l'écran affiche une ligne verte. En cas de détection d'un IMSI-catcher potentiel, elle devient une série de points jaunes, de tirets orange ou une ligne rouge continue.

### Heuristiques de détection de Rayhunter

**Rayhunter** utilise plusieurs algorithmes avancés pour détecter d'éventuelles activités d'IMSI-catchers :

#### Détection des requêtes IMSI
Cette heuristique repère les séquences suspectes où les stations cellulaires demandent l'identité de l'appareil (IMSI, International Mobile Subscriber Identity) sans respecter les procédures d'authentification appropriées. **Rayhunter** surveille le moment et le contexte de ces demandes, puis signale les schémas anormaux pouvant indiquer un équipement de surveillance.

Les réseaux cellulaires légitimes suivent des procédures d'authentification standardisées avant de demander des identifiants sensibles. Les IMSI-catchers contournent souvent ces procédures pour collecter rapidement les identités des appareils, ce qui crée des anomalies détectables dans la séquence d'authentification. Cette méthode est particulièrement efficace contre les IMSI-catchers passifs simples, qui ne font que collecter des informations sur les appareils.

#### Détection des déconnexions et des retours à la 2G
**Rayhunter** surveille en permanence les tentatives suspectes de déconnexion des appareils mobiles de réseaux 4G/5G sécurisés et de reconnexion à des réseaux 2G moins sûrs. Cette attaque est courante, car les réseaux 2G utilisent un chiffrement plus faible et sont plus faciles à intercepter.

Le système analyse les schémas de déconnexion et recherche une fréquence, un moment ou un contexte anormal pouvant indiquer une intention malveillante plutôt qu'une optimisation normale du réseau. Les réseaux légitimes peuvent parfois suggérer un retour à une génération antérieure pour des raisons de couverture ou de capacité, mais **Rayhunter** sait faire la différence avec une éventuelle surveillance.

#### Détection des retours via LTE SIB6/7
Les System Information Blocks (SIB) sont des messages diffusés par les réseaux cellulaires pour transmettre des informations de configuration aux appareils mobiles. **Rayhunter** surveille spécifiquement les messages SIB6 et SIB7, qui contiennent des informations sur les cellules voisines et la réorientation des fréquences.

Des acteurs malveillants peuvent diffuser de faux messages SIB6/7 pour forcer les appareils à abandonner des connexions 4G sécurisées et à rejoindre des réseaux 2G qu'ils contrôlent. **Rayhunter** analyse ces diffusions pour repérer les incohérences, les réorientations anormales et d'autres signes de stations de base frauduleuses qui tentent d'abaisser le niveau du réseau afin d'intercepter les communications.

#### Détection du chiffrement nul
Cette méthode de détection essentielle repère les cas où un réseau cellulaire propose une communication sans chiffrement, c'est-à-dire avec un chiffrement nul. Les réseaux cellulaires commerciaux légitimes ne devraient jamais proposer de connexion non chiffrée, car cela enfreindrait les normes de sécurité et les exigences réglementaires.

**Rayhunter** signale comme très suspect tout réseau proposant un chiffrement nul. *Un réseau légitime ne proposera jamais un chiffrement nul.* C'est un signe clair qu'un équipement de surveillance tente d'intercepter les communications en texte brut. Cette heuristique est particulièrement efficace contre les IMSI-catchers qui privilégient la collecte de données au maintien de l'apparence d'un réseau légitime.

#### Détection des SIB incomplets
Les stations de base cellulaires légitimes diffusent des System Information Blocks complets qui comprennent les données essentielles de configuration réseau. **Rayhunter** surveille les stations qui fournissent des informations système incomplètes ou manquantes, ce qui indique souvent un équipement de surveillance déployé à la hâte ou mal configuré.

Les IMSI-catchers n'implémentent souvent pas toutes les fonctions du réseau cellulaire et se limitent au minimum nécessaire pour connecter les appareils et intercepter les données. En détectant ces implémentations incomplètes, **Rayhunter** peut repérer des stations de base potentiellement malveillantes auxquelles manquent les fonctions attendues d'une infrastructure cellulaire légitime.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Schéma des cinq heuristiques Rayhunter : demande IMSI sans authentification, retour à la 2G, réorientation LTE SIB6/7, proposition de chiffrement nul et diffusion d'informations système incomplètes" >}}
## Acteurs de la menace et cibles potentielles

Comprendre qui déploie des IMSI-catchers et qui est visé permet d'évaluer votre modèle de menace personnel et de choisir une configuration adaptée de **Rayhunter**. Les acteurs ont des niveaux de sophistication différents et leurs stratégies de ciblage indiquent les types de surveillance que **Rayhunter** est conçu pour détecter.

### Services gouvernementaux et forces de l'ordre

**Niveau de sophistication de la menace** : avancé à professionnel
**Cibles principales** :
- Suspects criminels faisant l'objet d'une enquête
- Personnes d'intérêt dans des affaires de sécurité nationale
- Manifestants et militants pendant des rassemblements
- Surveillance générale de la population dans les zones hautement sécurisées
- Ressortissants étrangers et personnel diplomatique

**Schémas de détection** : Les IMSI-catchers employés par les gouvernements utilisent souvent des équipements sophistiqués susceptibles d'éviter les heuristiques de détection élémentaires. Ils emploient toutefois fréquemment des **attaques de retour à la 2G** et des **schémas de déconnexion** pour forcer les appareils à rejoindre des réseaux moins sûrs et faciliter l'interception. La détection des retours par LTE SIB6/7 et la surveillance des déconnexions de **Rayhunter** sont particulièrement efficaces contre les techniques de surveillance des forces de l'ordre.

**Scénarios typiques** :
- Surveillance lors de manifestations, de rassemblements ou d'événements publics
- Surveillance de lieux proches de bâtiments gouvernementaux ou d'infrastructures sensibles
- Surveillance ciblée de personnes faisant l'objet d'une enquête
- Opérations de surveillance aux frontières et dans les aéroports

### Services de renseignement nationaux et étrangers

**Niveau de sophistication de la menace** : professionnel à militaire
**Cibles principales** :
- Agents de renseignement étrangers et leurs sources
- Responsables gouvernementaux et personnel diplomatique
- Sous-traitants de la défense et chercheurs
- Dirigeants d'entreprises de secteurs stratégiques
- Journalistes couvrant des sujets de sécurité nationale
- Militants travaillant sur des questions politiques sensibles

**Schémas de détection** : Les équipements de renseignement sont conçus pour être discrets, mais la détection du chiffrement nul et la surveillance des SIB incomplets de **Rayhunter** peuvent repérer des opérations sophistiquées. Les services de renseignement utilisent souvent du matériel qui demande des **informations IMSI** pendant des opérations ciblées, ce qui déclenche les algorithmes de détection des requêtes IMSI de **Rayhunter**.

**Scénarios typiques** :
- Surveillance à long terme de cibles importantes pour le renseignement
- Espionnage industriel près des sièges d'entreprise
- Surveillance de diplomates et d'ambassades
- Opérations de contre-espionnage
- Services étrangers ciblant des sources nationales

### Organisations criminelles

**Niveau de sophistication de la menace** : élémentaire à intermédiaire
**Cibles principales** :
- Personnes fortunées à des fins d'enlèvement ou d'extorsion
- Concurrents commerciaux à des fins de collecte d'informations
- Forces de l'ordre enquêtant sur le crime organisé
- Témoins et informateurs dans des affaires pénales
- Personnes victimes de harcèlement, de traque ou de violence domestique

**Schémas de détection** : Les organisations criminelles utilisent généralement des IMSI-catchers commerciaux bon marché, qui déclenchent plusieurs heuristiques de **Rayhunter** en même temps. Ces appareils présentent souvent des **implémentations SIB incomplètes**, utilisent le **chiffrement nul** pour maximiser la collecte de données et lancent des **attaques agressives de retour à la 2G** en raison de leurs compétences techniques limitées.

**Scénarios typiques** :
- Suivi de cibles potentielles d'enlèvement ou de vol
- Surveillance des communications des forces de l'ordre lors d'opérations criminelles
- Espionnage industriel et collecte d'informations sur des concurrents
- Campagnes de traque et de harcèlement
- Intimidation de témoins et suivi de leur localisation

### Espionnage industriel et renseignement privé

**Niveau de sophistication de la menace** : intermédiaire à avancé
**Cibles principales** :
- Dirigeants d'entreprises concurrentes
- Équipes de recherche et développement
- Négociateurs de fusions et d'acquisitions
- Détenteurs de propriété intellectuelle
- Responsables de secrets commerciaux
- Lanceurs d'alerte et sources de menaces internes

**Schémas de détection** : Les opérations de surveillance commerciale utilisent souvent des équipements de milieu de gamme qui équilibrent coût et capacités. Ces installations déclenchent fréquemment la **détection de déconnexion** et des **alertes de requête IMSI** lorsqu'elles ciblent des personnes pendant des négociations commerciales ou des cycles de développement de produits.

**Scénarios typiques** :
- Surveillance lors de négociations de fusion ou d'acquisition
- Collecte d'informations sur les concurrents dans les salons et les conférences
- Opérations de vol de propriété intellectuelle
- Surveillance des employés et détection des menaces internes
- Collecte de données clients à des fins concurrentielles

### Détectives privés et sociétés de surveillance

**Niveau de sophistication de la menace** : élémentaire à intermédiaire
**Cibles principales** :
- Personnes faisant l'objet d'une enquête pour fraude à l'assurance
- Conjoints engagés dans une procédure de divorce
- Employés soupçonnés de faute
- Personnes impliquées dans un litige
- Célébrités et personnalités en vue

**Schémas de détection** : Les opérations de surveillance privée s'appuient généralement sur du matériel commercial peu personnalisable. Les contraintes de coût et les limites techniques font que ces systèmes déclenchent souvent les heuristiques de base de **Rayhunter**, en particulier la **détection du chiffrement nul** et la **surveillance des SIB incomplets**.

**Scénarios typiques** :
- Enquêtes sur des divorces et la garde d'enfants
- Surveillance liée à une fraude à l'assurance
- Enquêtes sur des fautes professionnelles
- Traque de célébrités et activité des paparazzi
- Enquêtes judiciaires et collecte de preuves

### Individus malveillants et hacktivistes

**Niveau de sophistication de la menace** : élémentaire à intermédiaire
**Cibles principales** :
- Ennemis personnels ou partenaires amoureux
- Personnalités publiques et célébrités
- Victimes prises au hasard dans des lieux publics
- Participants à des événements ou personnes présentes dans certains lieux
- Membres de communautés ou de groupes ciblés

**Schémas de détection** : Les acteurs individuels utilisent généralement des dispositifs IMSI-catcher élémentaires, souvent improvisés, qui déclenchent plusieurs algorithmes de **Rayhunter** simultanément. Ces dispositifs présentent souvent un **usage du chiffrement nul**, des **diffusions SIB incomplètes** et de grossières **tentatives de retour à la 2G**.

**Scénarios typiques** :
- Campagnes de traque et de harcèlement
- Usurpation d'identité et fraude financière
- Perturbation de l'activisme politique et des manifestations
- Cybercriminalité générale
- Surveillance opportuniste lors d'événements publics

### Évaluation des menaces et configuration de Rayhunter

Les **personnes à haut risque** (journalistes, militants, responsables gouvernementaux et dirigeants) devraient activer toutes les heuristiques de **Rayhunter** et choisir le mode d'affichage **haute visibilité** pour maximiser la détection.

Les **personnes à risque modéré** (utilisateurs généralement soucieux de leur vie privée) peuvent choisir le mode **discret** avec les principales heuristiques activées, pour une protection quotidienne sans attirer l'attention.

La **protection lors d'événements** (manifestations, réunions sensibles, voyages) justifie l'activation temporaire de toutes les méthodes de détection et des notifications afin de surveiller la présence d'activités de surveillance.

Comprendre votre modèle de menace permet d'optimiser **Rayhunter** selon votre niveau de risque et d'obtenir une couverture de détection adaptée aux acteurs susceptibles de vous prendre pour cible, vous ou vos activités.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Schéma des acteurs de la menace utilisant des IMSI-catchers, notamment les services gouvernementaux, les organisations criminelles et les espions industriels ciblant des appareils mobiles" >}}

## Efficacité de Rayhunter à l'ère de la 5G

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Schéma d'un téléphone 5G forcé par une attaque de retour vers un réseau 4G ou 3G surveillé, une technique toujours détectée par Rayhunter à l'ère de la 5G" >}}

Alors que les réseaux cellulaires passent à la 5G, des questions se posent sur la persistance de l'efficacité de **Rayhunter**, qui prend en charge la détection en 2G, 3G et 4G/LTE, mais pas les méthodes de surveillance natives à la 5G. Pour prévoir une stratégie de détection à long terme, il faut comprendre les limites actuelles et la pertinence de **Rayhunter** dans un monde 5G.

### Pourquoi Rayhunter reste efficace sur les réseaux 5G

#### La persistance des attaques de retour vers d'anciens réseaux
Le vecteur d'attaque principal détecté par **Rayhunter**, qui force les appareils à se connecter à des réseaux moins sûrs, reste pertinent avec le déploiement de la 5G. **Les IMSI-catchers continuent d'utiliser des attaques de retour à la 2G et à la 3G**, car :

- **Coûts d'implémentation plus faibles** : créer du matériel pour d'anciens protocoles demande beaucoup moins d'investissements que développer des systèmes compatibles avec la 5G.
- **Compatibilité plus large avec les appareils** : cibler la 2G/3G permet aussi de toucher les anciens appareils sans prise en charge de la 5G.
- **Méthodes d'attaque établies** : les techniques de surveillance des réseaux 2G/3G sont bien documentées et éprouvées.
- **Avantages réglementaires** : certaines technologies de surveillance plus anciennes peuvent subir moins de restrictions juridiques que les méthodes d'interception 5G avancées.

#### Rétrocompatibilité des réseaux
Les réseaux 5G préservent la **rétrocompatibilité avec la 4G/LTE**, et la plupart des appareils mobiles prennent en charge plusieurs générations simultanément. Cela laisse des possibilités aux attaques de retour vers d'anciens réseaux que **Rayhunter** est conçu pour détecter :

- **Basculement automatique** : les appareils repassent naturellement en 4G lorsque la couverture 5G est mauvaise, ce qui permet au matériel de surveillance d'intercepter cette transition.
- **Failles dans la négociation des protocoles** : des IMSI-catchers sophistiqués peuvent manipuler la négociation entre différentes générations de réseau.
- **Exploitation des lacunes de couverture** : des équipements placés stratégiquement dans des zones où la couverture 5G est incomplète peuvent forcer les appareils à rejoindre des réseaux 4G/LTE surveillés.

#### Déploiement progressif de la 5G
Le **déploiement lent d'une couverture 5G complète** maintiendra la pertinence de **Rayhunter** pendant plusieurs années :

- **Différences entre zones urbaines et rurales** : de nombreuses régions dépendent encore principalement de la 4G/LTE, où les capacités de détection de **Rayhunter** s'appliquent directement.
- **Limites de la couverture intérieure** : les signaux 5G traversent souvent mal les bâtiments. Les appareils reviennent alors sur les réseaux 4G que **Rayhunter** peut surveiller.
- **Voyages internationaux** : le déploiement de la 5G varie fortement selon les pays, la surveillance 4G/LTE reste donc une préoccupation pour les voyageurs.

#### Retard technologique des acteurs de la menace
Les cycles d'**acquisition et de déploiement des équipements de surveillance** accusent souvent un retard sur la technologie des réseaux commerciaux :

- **Délais d'approvisionnement gouvernemental** : les forces de l'ordre et les services de renseignement peuvent continuer d'utiliser du matériel 4G existant plusieurs années après le déploiement de la 5G.
- **Analyse coûts-bénéfices** : de nombreuses opérations atteignent leurs objectifs grâce à l'interception 4G/LTE moins coûteuse, ce qui réduit l'intérêt d'investir dans des systèmes 5G.
- **Besoins de formation et d'expertise** : utiliser un équipement de surveillance 5G nécessite des connaissances spécialisées que les organisations doivent acquérir.

### Limites de Rayhunter dans les environnements 5G réels

#### Angles morts de la surveillance 5G native
*C'est la principale limite de Rayhunter.* **Rayhunter ne peut pas détecter les opérations natives d'IMSI-catchers 5G** qui ne reposent pas sur une attaque de retour vers une ancienne génération :

- **Réseaux 5G autonomes (SA)** : lorsqu'un appareil se connecte à un réseau purement 5G sans revenir en 4G, **Rayhunter** ne peut pas surveiller ces communications.
- **Équipements de surveillance 5G avancés** : des acteurs sophistiqués disposant de technologies avancées pourraient intercepter des communications 5G sans déclencher les heuristiques de **Rayhunter**.
- **Exploitation du découpage réseau** : les fonctions de découpage réseau de la 5G pourraient servir à des fins de surveillance que **Rayhunter** ne détecte pas.

#### Fonctions de sécurité 5G renforcées
Les réseaux 5G intègrent des **mesures de sécurité améliorées** susceptibles de réduire l'efficacité des techniques de surveillance classiques :

- **Protocoles de chiffrement plus robustes** : la 5G met en œuvre des normes plus résistantes, plus difficiles à casser que celles des générations précédentes.
- **Procédures d'authentification améliorées** : une meilleure authentification des appareils sur les réseaux 5G pourrait compliquer la collecte des IMSI.
- **Surveillance de la sécurité réseau** : l'infrastructure 5G comporte de meilleures fonctions de détection des intrusions, qui peuvent identifier et contrer les tentatives de surveillance.

#### Évolution du comportement des appareils
À mesure que la 5G se répand, **le comportement des appareils mobiles peut évoluer** et affecter les capacités de détection de **Rayhunter** :

- **Moins de retours vers une ancienne génération** : de futures mises à jour logicielles pourraient mieux résister à ces attaques avec l'amélioration de la couverture 5G.
- **Priorité à la 5G** : les appareils pourraient privilégier davantage la 5G et se méfier des demandes d'utilisation d'anciens protocoles réseau.
- **Sensibilisation accrue à la sécurité** : les systèmes mobiles pourraient mieux détecter les comportements réseau suspects.

### Considérations stratégiques pour le déploiement de Rayhunter

#### Recommandations actuelles
Pour un déploiement immédiat et à court terme, **Rayhunter** offre des **capacités complètes de détection de la surveillance** :

- **Déploiement urbain** : même dans les grandes villes bien couvertes par la 5G, **Rayhunter** détecte les tentatives de surveillance visant les réseaux 4G/LTE.
- **Protection lors d'événements critiques** : pendant des manifestations, des réunions sensibles ou des activités à haut risque, **Rayhunter** offre des capacités de détection essentielles, quelle que soit la disponibilité de la 5G.
- **Sécurité en voyage** : **Rayhunter** reste très efficace pour détecter la surveillance pendant les déplacements nationaux et internationaux.

#### Stratégies pour anticiper l'avenir
Les organisations et les particuliers qui planifient la détection de la surveillance à long terme devraient envisager :

- **Approches de détection hybrides** : associer **Rayhunter** à d'autres outils de sécurité et techniques de surveillance assure une couverture complète de plusieurs vecteurs de menace.
- **Actualisation régulière de l'évaluation des menaces** : suivre l'évolution des technologies de surveillance aide à déterminer quand compléter ou remplacer les capacités de **Rayhunter**.
- **Soutenir le développement communautaire** : soutenir le développement open source de **Rayhunter** augmente les chances que de futures versions ajoutent la détection de la 5G.

#### Suivi de l'évolution technologique
La communauté **Rayhunter** et l'EFF continuent de rechercher des **capacités de détection de la surveillance 5G** :

- **Recherche sur l'analyse des protocoles** : l'étude continue des protocoles 5G pourrait révéler de nouvelles possibilités de détection pour de futures versions de **Rayhunter**.
- **Études de compatibilité matérielle** : évaluer si les appareils compatibles avec **Rayhunter** peuvent être améliorés pour détecter les tentatives de surveillance 5G.
- **Suivi du paysage des menaces** : suivre le développement et le déploiement d'équipements de surveillance 5G aide à définir les priorités de développement de **Rayhunter**.

**Rayhunter** reste un **outil essentiel de détection de la surveillance** dans les télécommunications actuelles et devrait rester pertinent pendant plusieurs années, tandis que la 5G se déploie progressivement et que les acteurs continuent d'utiliser des attaques éprouvées de retour vers d'anciennes générations.

### Réanalyser les enregistrements

**Rayhunter** améliore continuellement ses capacités de détection. Vous pouvez réanalyser les anciens enregistrements avec les heuristiques mises à jour. Cliquez sur "N warnings" dans l'interface Web, puis sélectionnez "re-analyze".

### Analyse sur ordinateur

Pour les utilisateurs avancés, **Rayhunter** inclut l'outil CLI `rayhunter-check` qui permet d'analyser les fichiers PCAP et QMDL sur ordinateur :

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Mode débogage
```

## Appareils pris en charge

**Rayhunter** prend en charge différents points d'accès mobiles avec des modems Qualcomm exposant l'interface `/dev/diag`.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Compatibilité des appareils Rayhunter par région" caption="Compatibilité des appareils et recommandations régionales pour les installations Rayhunter" >}}
### Appareils recommandés

Ces appareils ont été largement testés et sont très utilisés par la communauté **Rayhunter** :

#### Orbic RC400L (parfois commercialisé sous le nom Kajeet RC400L)
- **Région recommandée** : Amériques
- **Bandes prises en charge** :
  - 5G : n260/n261, n77, n2/5/48/66
  - 4G : 2/4/5/12/13/48/66
  - Mondial et itinérance : n257/n78
- **Disponibilité** : des appareils compatibles sont disponibles, notamment le **[nouvel Orbic RC400L avec Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** et le **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**
- **Fourchette de prix** : des modèles professionnels sont disponibles auprès de STS Collective

#### TP-Link M7350
- **Région recommandée** : Afrique, Europe et Moyen-Orient (fonctionne aussi dans les Amériques, mais coûte généralement plus cher)
- **Exigences particulières** : une carte SD formatée en FAT est requise pour les enregistrements
- **Disponibilité** : des modèles compatibles vérifiés sont proposés en **[TP-Link M7350 avec Rayhunter](https://stscollective.com/collections/rayhunter)**

### Appareils fonctionnels

Le fonctionnement de **Rayhunter** a aussi été confirmé sur ces appareils :

- **Wingtech CT2MHS01** (Amériques), **[disponible avec Rayhunter](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Amériques), **[disponible avec Rayhunter](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Afrique, Europe, Moyen-Orient), **[disponible avec Rayhunter](https://stscollective.com)**
- **PinePhone et PinePhone Pro** (monde entier), **[disponibles avec Rayhunter](https://stscollective.com)**
- **FY UZ801** (Asie, Europe), **[disponible avec Rayhunter](https://stscollective.com)**
- **Point d'accès Moxee** (Amériques), **[Moxee K779HSDL avec Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Notes d'installation par appareil

#### Orbic/Kajeet RC400L

L'Orbic RC400L est l'appareil d'origine pour lequel **Rayhunter** a été développé. Il est **[disponible avec Rayhunter](https://stscollective.com)** auprès de STS Collective.

**Méthodes d'installation** :
- **Par le réseau** : `./installer orbic` (recommandée, fonctionne en WiFi)
- **Par USB** : `./installer orbic-usb` (fournit l'accès ADB et un shell root)

**Mots de passe par défaut** :
- **Verizon RC400L** : le mot de passe administrateur est toujours le même que le mot de passe WiFi (disponible dans le menu de l'appareil)
- **Kajeet/Smartspot RC400L** : `$m@rt$p0tc0nf!g`
- **Appareils Moxee** : le mot de passe suit le format `12$XXX`, où XXX correspond aux 3 derniers chiffres du mot de passe WiFi (vérifiez sous la batterie)

**Accès au shell** : après l'installation, utilisez `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Ces appareils fonctionnent de manière fiable avec **Rayhunter** et sont **[disponibles avec Rayhunter](https://stscollective.com)**.

**Installation** : `./installer tplink` (aucun mot de passe administrateur n'est nécessaire)
**Stockage** : insérez une carte SD formatée en FAT avant l'installation
**Accès au shell** : `./installer util tplink-shell`

#### Appareils spécialisés

**PinePhone et PinePhone Pro** : compatibles dans le monde entier et **[disponibles avec Rayhunter](https://stscollective.com)**
**UZ801** : populaire en Asie et en Europe, **[disponible avec Rayhunter](https://stscollective.com)**
**Wingtech CT2MHS01** : appareil destiné aux Amériques, **[disponible avec Rayhunter](https://stscollective.com)**

### Ajouter de nouveaux appareils

**Rayhunter** pourrait prendre en charge tout appareil équipé d'un modem Qualcomm qui expose l'interface `/dev/diag`. Si vous souhaitez que **Rayhunter** prenne en charge un appareil, ouvrez une discussion dans le dépôt GitHub officiel.

## Documentation de l'API REST

**Rayhunter** fournit une API REST complète pour accéder par programmation à l'état de l'appareil, aux enregistrements et à la configuration. L'API permet de l'intégrer à d'autres outils de sécurité et systèmes de surveillance automatisés.

### Documentation officielle de l'API

La référence complète de l'API, avec les spécifications détaillées des points de terminaison, des exemples de requêtes et de réponses et les méthodes d'authentification, figure dans la **[documentation officielle de l'API REST Rayhunter](https://efforg.github.io/rayhunter/api-docs/)**.

### Points de terminaison de l'API

L'API **Rayhunter** est accessible à l'adresse `http://[device-ip]:8080/api/` et propose des points de terminaison pour :

- **État du système** : surveiller l'état de l'appareil et le fonctionnement de **Rayhunter**
- **Gestion des enregistrements** : démarrer, arrêter et télécharger des enregistrements
- **Récupération des alertes** : consulter les alertes de détection et les résultats d'analyse
- **Configuration** : mettre à jour les paramètres de **Rayhunter** par programmation
- **Contrôle des heuristiques** : activer ou désactiver certains algorithmes de détection
- **Informations sur l'appareil** : récupérer les caractéristiques et capacités de l'appareil
- **Surveillance du réseau** : accéder aux données cellulaires en temps réel
- **Journal des événements** : consulter les anciens événements de détection et les alertes

### Authentification

L'accès à l'API utilise la même authentification que l'interface Web. Sécurisez votre appareil **Rayhunter** et limitez l'accès aux utilisateurs autorisés.

### Exemples d'intégration

L'API REST **Rayhunter** peut être intégrée à diverses plateformes de surveillance de sécurité, systèmes SIEM et outils d'automatisation personnalisés. Consultez la **[documentation officielle de l'API](https://efforg.github.io/rayhunter/api-docs/)** pour des exemples complets et de bonnes pratiques.

## Dépannage

### Problèmes d'installation courants

**Problèmes de connexion USB** : essayez d'autres câbles ou ports USB. Des connexions USB défectueuses provoquent souvent des échecs d'installation. *C'est la cause la plus fréquente d'échec d'installation.*

**Problèmes de sécurité macOS** : si le message "No Orbic device found" apparaît, modifiez temporairement le paramètre "Allow accessories to connect" en "Always" dans les réglages de sécurité.

**Détection de l'appareil** : après l'installation, activez l'heuristique de test pour vérifier que **Rayhunter** fonctionne correctement.

### Obtenir de l'aide

Pour toute aide sur l'installation et le dépannage :
- Consultez la documentation officielle de **Rayhunter**
- Utilisez `./installer --help` et `./installer util --help` pour connaître les options des commandes
- Participez aux discussions de la communauté sur GitHub
- Contactez **[STS Collective](https://stscollective.com)** pour les questions de compatibilité des appareils

## Foire aux questions (FAQ)

### Questions générales

#### Qu'est-ce qu'un IMSI-catcher exactement et comment fonctionne-t-il ?
Un IMSI-catcher, aussi appelé StingRay, simulateur de station cellulaire ou fausse tour cellulaire, est un équipement de surveillance qui imite des stations cellulaires légitimes pour intercepter les communications des appareils mobiles. Il force les appareils voisins à se connecter à l'équipement malveillant plutôt qu'aux stations légitimes. Les opérateurs peuvent alors collecter les identifiants d'appareils (numéros IMSI), les données de localisation, les métadonnées d'appel et éventuellement intercepter les communications. **Rayhunter** détecte ces appareils en repérant les comportements anormaux du réseau cellulaire.

#### Rayhunter peut-il détecter tous les types d'équipements de surveillance ?
**Rayhunter** détecte spécifiquement les IMSI-catchers et simulateurs de stations cellulaires qui fonctionnent sur les réseaux 2G, 3G et 4G/LTE. Il ne détecte pas les autres formes de surveillance, comme la surveillance WiFi, les traceurs GPS, l'observation physique ou la surveillance 5G native sans attaque de retour vers une génération antérieure. **Rayhunter** est un élément d'une stratégie complète de protection de la vie privée.

#### L'utilisation de Rayhunter est-elle légale ?
Dans la plupart des juridictions, l'utilisation de **Rayhunter** est légale, car il s'agit d'un outil de surveillance passive qui n'interfère pas avec les réseaux cellulaires ni les autres appareils. Il analyse simplement les signaux cellulaires que reçoit naturellement votre appareil. Les lois locales varient, vérifiez donc la réglementation de votre région. L'EFF a développé **Rayhunter** comme un outil légitime de protection de la vie privée.

### Questions techniques

#### Pourquoi Rayhunter nécessite-t-il une carte SIM sans avoir besoin d'un forfait actif ?
La carte SIM contient l'International Mobile Subscriber Identity (IMSI), nécessaire à l'authentification de l'appareil sur les réseaux cellulaires et aux échanges de protocole que **Rayhunter** surveille. Sans carte SIM, l'appareil ne peut pas se connecter aux réseaux cellulaires et **Rayhunter** n'a pas d'activité réseau à analyser pour repérer d'éventuels schémas suspects.

#### Quelle quantité de données Rayhunter consomme-t-il en fonctionnement normal ?
**Rayhunter** utilise peu de données pour la surveillance de base, car il analyse surtout les informations des protocoles cellulaires et non le trafic Internet. La consommation augmente si vous activez les notifications à distance via ntfy ou utilisez simultanément l'appareil comme point d'accès. La surveillance seule consomme une bande passante négligeable.

#### Puis-je utiliser Rayhunter pendant que l'appareil sert de point d'accès mobile ?
Oui, **Rayhunter** peut fonctionner en même temps que le point d'accès mobile. Un forfait cellulaire actif est nécessaire. La surveillance de **Rayhunter** fonctionne indépendamment du point d'accès, mais l'utilisation simultanée des deux fonctions consomme davantage de batterie.

#### Quelle est la différence entre les installations WiFi et USB ?
La **méthode WiFi** (recommandée à la plupart des utilisateurs) installe **Rayhunter** via l'interface sans fil de l'appareil et offre les fonctions standard. La **méthode USB** donne aux utilisateurs avancés accès à Android Debug Bridge (ADB) pour le débogage, mais elle est plus complexe et inutile pour une installation classique.

### Questions sur les appareils et la compatibilité

#### Pourquoi Rayhunter ne prend-il en charge que certains appareils ?
**Rayhunter** nécessite un appareil équipé d'un modem Qualcomm qui expose l'interface `/dev/diag`, donnant accès aux informations de protocole cellulaire. La plupart des appareils grand public ne proposent pas cette interface pour des raisons de sécurité. Les appareils pris en charge ont été testés et leur compatibilité avec les exigences de **Rayhunter** a été confirmée.

#### Puis-je installer Rayhunter sur un smartphone classique ?
Non. **Rayhunter** ne peut pas être installé sur les smartphones classiques. Il nécessite des points d'accès mobiles spécialisés équipés de certains modems Qualcomm exposant des interfaces de diagnostic. Parmi les appareils pris en charge figurent l'Orbic RC400L, le TP-Link M7350 et plusieurs autres modèles de points d'accès mobiles.

#### Que se passe-t-il si j'essaie d'installer Rayhunter sur un appareil incompatible ?
L'installateur **Rayhunter** détecte l'appareil et refuse généralement de s'installer sur du matériel incompatible. Forcer l'installation sur un appareil non pris en charge peut l'endommager ou le rendre inutilisable. Vérifiez toujours la compatibilité avant l'installation.

#### Faut-il des appareils différents selon les régions ?
Oui. Les bandes de fréquences cellulaires varient selon les régions. L'Orbic RC400L est optimisé pour les réseaux des Amériques, tandis que le TP-Link M7350 fonctionne bien en Europe, en Afrique et au Moyen-Orient. Les informations de compatibilité des appareils **Rayhunter** comprennent des recommandations régionales adaptées à votre emplacement.

### Questions sur l'utilisation et la configuration

#### Comment savoir si mon appareil Rayhunter fonctionne correctement ?
Activez l'heuristique de test dans les paramètres de **Rayhunter**. Elle déclenche une alerte chaque fois que l'appareil détecte une station cellulaire, ce qui confirme le fonctionnement du système. En fonctionnement normal, l'écran doit afficher une ligne verte. N'oubliez pas de désactiver l'heuristique après le test, car elle produit de nombreuses alertes.

#### Que faire si Rayhunter déclenche une alerte ?
Lorsque **Rayhunter** détecte une activité suspecte, notez d'abord votre emplacement et les circonstances. L'optimisation du réseau ou des problèmes d'équipement peuvent provoquer de faux positifs. Si les alertes persistent au même endroit ou pendant des activités sensibles, envisagez de vous déplacer et consultez les détails de l'alerte dans l'interface Web.

#### À quelle fréquence dois-je mettre Rayhunter à jour ?
**Mettez Rayhunter à jour chaque mois.** Consultez la page des versions pour vérifier l'arrivée de nouvelles heuristiques et améliorations de compatibilité, ajoutées régulièrement. L'EFF améliore continuellement les capacités de **Rayhunter** face à l'évolution des techniques de surveillance. La mise à jour suit la même procédure que l'installation initiale.

#### Rayhunter peut-il protéger plusieurs personnes en même temps ?
**Rayhunter** détecte les IMSI-catchers à proximité et peut potentiellement protéger plusieurs personnes dans sa portée, généralement quelques centaines de mètres selon la puissance du signal. Toutefois, toute personne qui souhaite sérieusement détecter la surveillance devrait envisager son propre appareil **Rayhunter** pour bénéficier d'une protection maximale et garder le contrôle de la configuration.

### Questions de sécurité et de confidentialité

#### L'utilisation de Rayhunter me rend-elle plus visible pour les services de surveillance ?
**Rayhunter** fonctionne de manière passive et n'émet aucun signal qui permettrait aux équipements de surveillance de l'identifier. Toutefois, utiliser un outil de sécurité indique une préoccupation pour la vie privée. Les avantages de la détection dépassent généralement les risques, surtout pour les personnes à haut risque comme les journalistes et les militants.

#### Les équipements de surveillance peuvent-ils détecter que j'utilise Rayhunter ?
**Rayhunter** est un système de surveillance passif qui n'émet pas de signaux identifiants. Les opérateurs de surveillance ne peuvent pas détecter l'utilisation de **Rayhunter** au niveau du protocole cellulaire. L'observation physique de l'appareil ou l'analyse du trafic réseau peut toutefois révéler l'utilisation de **Rayhunter** si les notifications à distance sont activées.

#### Quelles informations Rayhunter collecte-t-il à mon sujet ?
**Rayhunter** analyse les informations des protocoles cellulaires et stocke les alertes de détection localement sur l'appareil. Il ne collecte aucune information personnelle, aucun contenu de communication ni aucune donnée de localisation au-delà de ce qui est nécessaire aux algorithmes de détection. Toutes les données restent sur l'appareil, sauf si vous activez les notifications à distance.

### Questions avancées

#### Puis-je analyser les données Rayhunter sur mon ordinateur ?
Oui. **Rayhunter** comprend l'outil en ligne de commande `rayhunter-check`, qui permet d'analyser les fichiers PCAP et QMDL enregistrés sur un ordinateur. Les utilisateurs avancés peuvent ainsi examiner en détail les événements de détection et enquêter sur les activités suspectes.

#### Comment Rayhunter fonctionne-t-il dans les zones urbaines denses ?
Les nombreuses stations cellulaires légitimes des zones urbaines denses peuvent augmenter les faux positifs, car l'optimisation du réseau et les changements de station se produisent plus souvent. Les algorithmes de **Rayhunter** distinguent le comportement normal du réseau de la surveillance, mais les utilisateurs de zones denses devront peut-être régler la sensibilité.

#### Rayhunter fonctionne-t-il lors de voyages internationaux ?
L'efficacité de **Rayhunter** en voyage dépend de la compatibilité de l'appareil avec les bandes cellulaires locales et les accords d'itinérance. Les algorithmes fonctionnent partout dans le monde, mais vérifiez que votre appareil prend en charge les fréquences utilisées dans le pays de destination. Une itinérance internationale peut être nécessaire pour toutes les fonctions.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Une personne consulte les alertes Rayhunter sur un ordinateur portable et transporte un point d'accès mobile dans une ville où se trouvent des antennes cellulaires" >}}

______

**Rayhunter** représente une avancée importante pour la protection de la vie privée et la détection de la surveillance. En flashant et configurant correctement **Rayhunter** sur un appareil compatible, vous pourrez détecter des IMSI-catchers et protéger vos communications mobiles contre la surveillance non autorisée.

Que vous soyez journaliste, militant, professionnel de la sécurité ou simplement soucieux de votre vie privée, **Rayhunter** fournit des outils pour préserver la sécurité mobile dans un monde de plus en plus surveillé. Pour trouver des appareils compatibles vérifiés, consultez les options **[Rayhunter à vendre](https://stscollective.com)** de fournisseurs de matériel de sécurité fiables.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Achetez des appareils Rayhunter et économisez 20 %
{{< /centerbutton >}}

## Références

- [Dépôt GitHub officiel de Rayhunter](https://github.com/EFForg/rayhunter)
- [Dernière version de Rayhunter](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, fournisseur d'équipements Rayhunter](https://stscollective.com)
