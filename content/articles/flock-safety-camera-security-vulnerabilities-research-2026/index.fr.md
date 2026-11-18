---
title: "Vulnérabilités des caméras Flock Safety : plus de 50 failles découvertes"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Cette enquête sur les vulnérabilités des caméras Flock Safety couvre les identifiants exposés, les protections faibles, l'accès physique et les limites du processus de divulgation."
genre: ["Recherche en sécurité", "Analyse de vulnérabilités", "Technologies de surveillance", "Cybersécurité", "Protection de la vie privée", "Sécurité de l'IoT", "Sécurité physique", "Sécurité réseau", "Infrastructures critiques", "Technologies gouvernementales"]
tags: ["Vulnérabilités Flock Safety", "Sécurité ALPR", "Piratage de caméras", "Failles de sécurité IoT", "Mots de passe codés en dur", "Vulnérabilités Android Things", "Exploitation par accès physique", "Sécurité réseau", "Défaillances du chiffrement", "Atteintes à la vie privée", "Divulgations de CVE", "Recherche en sécurité", "Recherche GainSec", "Enquête Ben Jordan", "Sécurité des caméras de surveillance", "Failles des technologies gouvernementales", "Vulnérabilités critiques", "Divulgation responsable", "Analyse de cybersécurité", "Technologies des forces de l'ordre", "Sécurité de la sûreté publique", "Point d'accès sans fil", "Contournement de l'authentification", "Identifiants en clair", "Fuites RF", "Attaque Tempest", "Divulgation d'informations", "Accès au shell root", "Exécution de code à distance", "Audit de sécurité", "Évaluation de vulnérabilités", "Risque pour la sécurité nationale", "Enquête du Sénat", "Programme de primes aux bogues", "Vulnérabilité zero-day", "Développement d'exploits", "Tests d'intrusion", "Livre blanc de sécurité", "Couverture de 404 Media", "Recherche indépendante", "Sécurité matérielle", "Analyse de micrologiciel", "Exploitation de systèmes"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Une caméra de surveillance de haute technologie apparaît avec des reflets bleus et verts sur un fond sombre. Des formes et des lignes abstraites l'entourent pour représenter des vulnérabilités de sécurité numérique."
coverCaption: "Des failles de sécurité critiques exposent plus de 80 000 caméras de surveillance à un accès non autorisé"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Plus de 50 vulnérabilités critiques exposent le plus grand réseau privé de surveillance du pays**

## Introduction : une crise de sécurité nationale

À la fin de 2024 et pendant toute l'année 2025, des chercheurs indépendants en sécurité ont découvert ce qui pourrait être **la défaillance de sécurité la plus importante de l'histoire des technologies de surveillance utilisées par les forces de l'ordre aux États-Unis**. Plus de **50 vulnérabilités critiques** ont été découvertes dans les systèmes de caméras de Flock Safety. Ces caméras photographient et suivent chaque jour plus de **150 millions de véhicules** dans plus de **80 000 déploiements** à travers le pays.

Cet article présente une analyse technique complète de ces vulnérabilités, fondée sur :
- **Le livre blanc officiel de GainSec**, « Examining the Security Posture of an Anti-Crime Ecosystem » (51 constats, 22 CVE attribués, 8 en attente)
- **L'enquête journalistique de Ben Jordan** et ses tests pratiques de sécurité
- **Les reportages de 404 Media** sur les flux vidéo de caméras accessibles publiquement
- **Les réponses officielles** de Flock Safety et de sénateurs américains
- **Les divulgations publiées dans la National Vulnerability Database** (NVD)
- **L'image du système de fichiers de septembre 2026**, publiée par Distributed Denial of Secrets, accompagnée d'une analyse technique détaillée de Micah Lee et d'une enquête conjointe de WIRED et de 404 Media

Pour comprendre **pourquoi ces caméras sont déployées** et leurs **conséquences pour la vie privée**, consultez notre article : **[Vidéosurveillance par les caméras Flock Safety : déploiement, enjeux de confidentialité et moyens de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Pour savoir **comment détecter ces caméras**, consultez : **[Projet de détection Flock-You : guide de matériel anti-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## L'ampleur du problème

### Échelle de l'infrastructure vulnérable

En mai 2026 :
- **Plus de 80 000 caméras Flock Safety** déployées aux États-Unis
- **Plus de 5 000 villes et communes** utilisent les services de Flock
- **Plus de 3 500 services des forces de l'ordre** ont accès au système
- **Plus de 22 000 utilisateurs des forces de l'ordre** consultent les bases de données
- **Des milliards de points de données** conservés dans des bases de données consultables

### Chronologie des vulnérabilités

- **Fin 2024** : première découverte de vulnérabilités par le chercheur en sécurité Jon « GainSec » Gaines
- **Février 2025** : début de la divulgation responsable auprès de Flock Safety
- **Avril 2025** : publication des premières attributions de CVE
- **Novembre 2025** : publication du livre blanc officiel, qui recense 51 constats
- **Décembre 2025** : Ben Jordan démontre les vulnérabilités dans une vidéo
- **Janvier 2026** : 404 Media découvre plus de 60 flux de caméras accessibles au public
- **Février 2026** : des sénateurs américains demandent une enquête de la FTC
- **Mai 2026** : le processus de divulgation se poursuit

### Catégories de vulnérabilités

Les plus de 50 vulnérabilités couvrent plusieurs catégories :
1. **Authentification et autorisation** (mots de passe codés en dur, absence d'authentification multifacteur)
2. **Cryptographie et chiffrement** (données non chiffrées au repos et en transit)
3. **Sécurité réseau** (points d'accès Wi-Fi exposés, identifiants en clair)
4. **Sécurité physique** (attaques déclenchées par pression sur un bouton, ports USB exposés)
5. **Confidentialité des données** (collecte non autorisée, conservation prolongée)
6. **Conception système** (logiciels obsolètes, contrôles d'accès insuffisants)
7. **Divulgation d'informations** (clés API exposées, flux de caméras publics)

______

## L'image du système de fichiers de septembre 2026

**En septembre 2026, l'organisation à but non lucratif Distributed Denial of Secrets, qui défend la transparence, a publié des images complètes du système de fichiers d'une caméra Flock en service.** Un collectif se faisant appeler **stegan0gram** a dévissé le matériel de son poteau, copié le stockage interne et publié les images. **404 Media** et **WIRED** ont mené une enquête conjointe, tandis que le chercheur en sécurité **Micah Lee** a publié une analyse technique détaillée du contenu.

Toutes les découvertes précédentes de cet article provenaient d'un appareil de laboratoire utilisé par un chercheur ou d'un appareil acheté. Ces données proviennent d'une caméra en service dans une municipalité. Elles constituent donc la preuve la plus solide publiée à ce jour.

*La caméra n'a pas été compromise par le réseau. Elle a été retirée physiquement.*

### Contenu de l'image

La publication comprend trois images de partitions, chacune révélant un aspect différent du problème.

| Partition | Taille | Importance |
|-----------|--------|------------|
| **system** | 1,5 Go | Image système Android contenant **19 applications développées par Flock**, dont `flock-sambuca`, `flock-collins` et `flock-phone-home` |
| **persist** | 32 Mo | Identifiants de l'appareil dans `flock/auth0/auth0_cred`, sur une **partition non chiffrée conçue pour survivre à une réinitialisation d'usine** |
| **media** | 18 Go | Journaux et images dans un conteneur dont **la clé de déchiffrement est stockée sur la même partition** |

### Le problème des identifiants est confirmé

L'image permet de savoir si les identifiants codés en dur sont théoriques ou déployés. Ils sont bien déployés.

**Une clé API donnant accès au serveur principal de Flock est codée en dur dans les binaires des applications.** Elle se trouve dans une classe nommée `CameraSettings`, au sein de `com.flocksafety.android.common.lib`. Flock intègre cette bibliothèque partagée dans les 19 applications, de sorte que chacune contient la clé. L'application `flock-sambuca` l'utilise pendant le provisionnement.

**Le flux d'authentification fonctionne ainsi :**

1. Chaque caméra demande des identifiants à un serveur de Flock et s'identifie avec son **adresse MAC**
2. Le service de connexion **Okta Auth0** de Flock renvoie un `FlockAuth0Token` de courte durée
3. La caméra stocke les identifiants reçus **en clair**

L'identifiant client et le secret client Auth0 se trouvent sur la **partition `/persist` non chiffrée**, dans un fichier conçu pour survivre à une réinitialisation d'usine. Un attaquant récupère d'abord la partition persist, car rien ne la protège.

La [vulnérabilité critique no 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) décrit plus largement les secrets codés en dur sur la plateforme.

### La clé de chiffrement livrée avec le verrou

Flock affirme que ses caméras sont protégées par un **chiffrement sur l'appareil**. L'image montre comment cela fonctionne en pratique.

La partition media de 18 Go se trouve bien dans un conteneur chiffré. Mais la clé de déchiffrement est sur la même partition, dans un fichier dont le nom se termine par `.key`. Le collectif stegan0gram a récupéré la clé, déverrouillé le conteneur et lu son contenu. **Les images sont chiffrées comme l'est une boîte verrouillée dont la clé est scotchée sur le couvercle.**

Les journaux récupérés ont également révélé la position de la caméra. Les coordonnées GPS apparaissent **155 fois** dans les journaux et sont regroupées dans un rayon d'environ 100 mètres, une dérive normale pour un récepteur fixé à un poteau. Elles indiquent **Wauwatosa, dans le Wisconsin**, une banlieue de Milwaukee où la caméra était installée sur N Mayfair Road. Micah Lee a comparé les journaux à Google Street View et identifié l'appareil précis grâce à son numéro de série et à son adresse MAC.

*Le chiffrement au repos ne sert à rien si la clé est stockée à côté du texte chiffré.*

### La réponse de Flock

La réponse de Flock reprend sa position face aux premières découvertes de GainSec. Un porte-parole a déclaré :

> « Flock prend la sécurité au sérieux et maintient une politique publique de divulgation des vulnérabilités qui permet aux chercheurs de nous signaler directement les vulnérabilités potentielles. Nous n'avons reçu aucun signalement par cette procédure et, au vu des informations limitées qui nous ont été fournies, nous n'avons pas assez de détails pour évaluer les affirmations formulées. »

Cette réponse s'accorde difficilement avec la chronologie. Les vulnérabilités du système d'exploitation des caméras ont été corrigées publiquement en **2018 et 2021**, et les normes de stockage des identifiants et de gestion des clés n'ont pas changé depuis bien avant la livraison de la caméra. **Examiner dix ans d'historique public des vulnérabilités ne nécessite aucun signalement externe.**

Flock a également déclaré que le retrait et l'analyse de la caméra étaient illégaux, ce qui est le cas au regard de la loi actuelle. Les constats de sécurité restent toutefois valables, quelles que soient les conditions d'obtention du matériel.

### Pourquoi cette découverte compte plus que les recherches précédentes

Le livre blanc de GainSec documentait 51 constats sur des appareils obtenus légalement. Flock contestait leur gravité et soutenait qu'un accès physique était nécessaire.

Cette image écarte ces réserves. Dans son état de production par défaut, sans modification de ses opérateurs, une caméra contient des identifiants d'infrastructure en clair, des clés stockées à côté des données qu'elles protègent et un système d'exploitation privé de huit années de mises à jour de sécurité. **Aucun exploit n'était nécessaire. Une clé à molette suffisait.**

______

## Le parc d'appareils

Flock vend une gamme de produits, et non une seule caméra. Les propriétés de sécurité diffèrent selon l'appareil. Les caractéristiques ci-dessous proviennent des démontages de GainSec et de l'analyse des micrologiciels compilée par la communauté de détection sur **[WiFi Mothership](https://wifimothership.com/flock)**.

| Appareil | Rôle | Plateforme | Système d'exploitation |
|--------|------|----------|-----|
| **Falcon** | Caméra ALPR alimentée par énergie solaire | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Caméra ALPR alimentée par câble | Identique à Falcon | Android 8.1 |
| **Raven** | Détection audio de coups de feu et d'appels de détresse | ESP32-WROOM-32D avec DSP Syntiant NDP120-B0 | FreeRTOS / ESP-IDF |
| **Bravo** | Boîtier informatique d'IA en périphérie | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, noyau 5.4.180** |
| **Picard** | Ancien boîtier informatique | Remplacé par Bravo | |
| **Condor** | Caméra PTZ | Documentation incomplète | |
| **Alpha** | Drone autonome | Conçu par Flock, conforme à la NDAA | Pilote automatique propriétaire |
| **Aerodome M350** | Ancien drone | DJI Matrice M350 / M300 RTK | Micrologiciel DJI |
| **Remorque LPR (ATS-5)** | Plateforme ALPR mobile | Châssis All Traffic Solutions avec caméra Flock | Identique à Falcon |
| **Wing** | Pont logiciel pour caméras tierces | Aucun, il encapsule des caméras IP existantes | |

*L'écart entre les générations saute d'abord aux yeux. Le boîtier informatique fonctionne sous Android 13, alors que les caméras qu'il dessert utilisent Android 8.1, un système d'exploitation publié en 2017.*

**Falcon mérite une attention particulière.** Elle gère la charge de travail ALPR, utilise toujours Android 8.1 et stocke ses données sur une **mémoire eMMC de 32 Go non chiffrée**. Le collectif stegan0gram a récupéré les médias et les journaux sur cette même mémoire. Sparrow utilise la même plateforme avec une alimentation filaire.

**Bravo présente le cas inverse.** Ce boîtier informatique récent fonctionne sous Android 13 et exécute l'inférence IA pour les flux des caméras. Il montre que l'entreprise est prête à livrer des logiciels récents lorsqu'elle le décide.

## Identifiants CVE vérifiés

Quinze CVE ont été attribués aux familles Falcon, Sparrow, Raven et Bravo. Chaque identifiant ci-dessous a été vérifié dans son **dossier CVE.org** en septembre 2026, plutôt que repris d'une source secondaire.

### Détection des coups de feu et appareils audio

| CVE | Constat | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Mot de passe de connexion codé en dur | 2.2 |
| **CVE-2025-47819** | Interface de débogage sur puce avec contrôle d'accès inadéquat | 6.4 |
| **CVE-2025-47820** | Stockage de code en clair | 2.0 |
| **CVE-2025-47821** | Mot de passe système codé en dur | 2.2 |

Les quatre vulnérabilités touchent les appareils de détection des coups de feu **antérieurs à la version 1.3**.

### Lecteurs de plaques d'immatriculation

| CVE | Constat | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Interface de débogage sur puce avec contrôle d'accès inadéquat | 6.4 |
| **CVE-2025-47823** | Mot de passe système codé en dur | 2.2 |
| **CVE-2025-47824** | Stockage de code en clair | 2.0 |

Ces trois vulnérabilités touchent les micrologiciels des lecteurs de plaques d'immatriculation **jusqu'à la version 2.2 incluse**.

### Failles des applications présentes dans toute la flotte

| CVE | Constat | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | L'application Collins expose des points de terminaison administratifs sur le **port 8080 sans authentification** : `/reboot`, `/logs`, `/crashpack` et `/adb/enable`. Le dernier active ADB sur TCP sans confirmation de débogage, ce qui donne un shell à un attaquant présent sur le même réseau | **9.8 CRITIQUE** |
| **CVE-2025-59407** | L'application DetectionProcessing embarque un magasin de clés Java avec son **mot de passe codé en dur**. Ce magasin contient une clé privée | **9.8 CRITIQUE** |
| **CVE-2025-59405** | L'application Peripheral contient une clé API DataDog en clair | 7.5 |
| **CVE-2025-59409** | Les micrologiciels de production Falcon et Sparrow sont livrés avec des **identifiants Wi-Fi de développement en clair** | 7.5 |
| **CVE-2025-59406** | L'application Pisco intègre un **secret client Auth0** en clair | 6.2 |

### Boîtier informatique Bravo

| CVE | Constat | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Accepte le chargeur Firehose par défaut Thundercomm TurboX 6490, ce qui permet de flasher le micrologiciel et de copier les partitions | 5.4 |
| **CVE-2025-59404** | Livré avec le chargeur de démarrage déverrouillé, ce qui contourne Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Livré avec Secure Boot désactivé | 7.3 |

**Quatre de ces vulnérabilités utilisent un vecteur d'attaque réseau avec un score d'au moins 7,5. Aucune ne nécessite donc d'accès physique.** L'identifiant CVE-2025-59403 désigne le chemin API sans authentification, y compris l'appel `/adb/enable` utilisé par la [vulnérabilité critique no 1](#critical-vulnerability-1-button-press-wireless-access-point) pour obtenir un shell root.

*Les dossiers CVE comptent aussi pour une deuxième raison. Ils confirment le problème des secrets en clair dans des registres indépendants, et la page d'alerte de sécurité de Flock figure comme référence dans les dossiers Raven et LPR.*

______

## Vulnérabilité critique no 1 : point d'accès sans fil déclenché par un bouton {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Gravité** : CRITIQUE (CVSS 9.8)

### L'exploitation

La vulnérabilité la plus alarmante découverte permet à **toute personne ayant un accès physique** à une caméra Flock Safety d'en prendre le contrôle complet en moins de 60 secondes :

**Étape 1** : appuyer **trois fois** sur le bouton à l'arrière de la caméra Falcon/Sparrow
**Étape 2** : l'appareil crée un point d'accès Wi-Fi ouvert
**Étape 3** : se connecter au réseau Wi-Fi (mot de passe codé en dur : indiqué dans le livre blanc de GainSec)
**Étape 4** : envoyer la commande d'activation d'ADB (Android Debug Bridge)
**Étape 5** : se connecter via ADB et obtenir un shell root
### Détails techniques

```
Appareil : caméra ALPR Flock Safety Falcon/Sparrow
Matériel : Android Things 8.0/8.1 (fin du support en 2021)
Vecteur d’attaque : séquence de pressions physiques sur le bouton
Authentification : mot de passe WiFi codé en dur (identique sur tous les appareils)
Impact : compromission complète de l’appareil, exfiltration des données et installation de logiciel malveillant
```

### Ce que cela permet

Une fois l'accès au shell obtenu, un attaquant peut :
- **Extraire toutes les images stockées** (y compris celles de personnes, pas seulement de véhicules)
- **Modifier ou supprimer les preuves** enregistrées sur l'appareil
- **Installer un logiciel malveillant persistant** (qui survit aux redémarrages)
- **Cloner l'identité de l'appareil** pour usurper celle-ci
- **Intercepter et modifier** les flux vidéo
- **Utiliser l'appareil comme client de botnet** pour lancer des attaques DDoS
- **Capturer les identifiants Wi-Fi** des appareils voisins (attaque par faux point d'accès)
- **Désactiver la caméra** ou provoquer un déni de service

### Démonstration

Le chercheur en sécurité Ben Jordan a démontré cet exploit sur YouTube. Il a montré :
- La connexion au point d'accès Wi-Fi en **moins de 30 secondes**
- L'obtention d'un shell root en **moins de 60 secondes au total**
- L'accès complet au système de fichiers, aux images stockées et à la mémoire système
- La possibilité d'installer n'importe quelle application Android

**Citation de la démonstration** :
> « Le mot de passe de ce point d'accès est [REDACTED], tout en minuscules. Toutes les caméras que nous avons essayées ont exactement ce mot de passe codé en dur. Ensuite, il suffit d'envoyer une commande pour activer ADB... en moins de 30 secondes environ, on peut obtenir un shell complet sur l'appareil et accéder à tout. »

### Réponse du fournisseur

Flock Safety a d'abord affirmé que la vulnérabilité ne touchait que les **appareils non connectés au cloud**, qu'elle a comparés à **« un iPhone volé dans un camion avant sa première connexion »**.

*Cette affirmation a été réfutée.* Les chercheurs ont reproduit la vulnérabilité **sur des appareils connectés au cloud**, sur plusieurs modèles de caméras présentant une **vulnérabilité identique**, et sur des appareils obtenus de **sources différentes**. Tous présentaient la faille.

______

## Vulnérabilité critique no 2 : système d'exploitation Android obsolète

### CVE-2025-47822 à CVE-2025-47824

**Gravité** : MOYENNE à FAIBLE (CVSS 6.4, 2.2 et 2.0)

### Le problème

Les caméras Flock Safety utilisent **Android Things 8.0 ou 8.1**, qui :
- A été **abandonné par Google en 2021**
- Ne reçoit **AUCUNE mise à jour de sécurité depuis 2021**
- Compte **plus de 900 vulnérabilités publiées** en 2026
- N'est plus pris en charge depuis **plus de 5 ans**

### Analyse technique

**Système d'exploitation** : Android Things 8.0/8.1  
**Fin de vie** : janvier 2021  
**Vulnérabilités connues** : plus de 900  
**Correctifs de sécurité** : aucun depuis la fin de vie  
**Appareils concernés** : boîtiers informatiques Falcon, Sparrow, Condor et Bravo

### Ce que révèle l'image de septembre 2026

Les images du système de fichiers publiées en septembre 2026 indiquent les versions précises d'une caméra en service, plutôt que celles d'un appareil de laboratoire.

| Composant | Version sur la caméra | État |
|-----------|----------------------|--------|
| **Android** | 8.1, compilation datée du 5 juin 2025 | Niveau de correctif de sécurité **2018-06-05** |
| **Noyau Linux** | 3.18.71 | Publié en 2017. La série 3.18 s'est achevée à la version 3.18.140 en mai 2019 |
| **Version actuelle d'Android** | Android 17, juin 2026 | Neuf versions majeures plus récente |

La compilation de la caméra est récente. **Le système d'exploitation sous-jacent ne l'est pas**. Le niveau de correctif indique que l'appareil n'a reçu aucune mise à jour de sécurité Android depuis **huit ans**. Le noyau a **69 versions de correctifs de retard** par rapport à la fin même de sa branche de maintenance, ce qui représente plus de neuf ans de correctifs manquants.

### Deux vulnérabilités présentes dans cette compilation

Micah Lee a identifié deux failles connues du public qui touchent des composants livrés avec la caméra. Les dates des correctifs prouvent que la caméra les précède toutes les deux.

| CVE | Composant | Effet | Date du correctif |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Pilote GPU Qualcomm Adreno | Use-after-free permettant à **tout code sur l'appareil, y compris une application sans privilèges, de corrompre la mémoire du noyau et de prendre le contrôle total** | Mai 2021 |
| **CVE-2018-9568**, « WrongZone » | Gestion des sockets du noyau Linux | Confusion de types via IPv6 permettant à un programme **d'obtenir les privilèges root**. Un exploit public existe | Décembre 2018 |

Les deux vulnérabilités ont été corrigées des années avant la compilation du micrologiciel de cette caméra. **Aucune ne nécessite un accès physique, car elles sont accessibles depuis des logiciels qui fonctionnent déjà sur l'appareil.** La réserve de proximité utilisée par Flock pour minimiser les constats de GainSec ne s'applique à aucune des deux.

### Comparaison avec les appareils grand public

À titre de comparaison :
- Votre **smartphone** cesse de recevoir des mises à jour après environ cinq ans et les fabricants **arrêtent de le vendre**
- Une **caméra de sécurité domestique** qui utilise un logiciel vieux de cinq ans serait considérée comme **gravement vulnérable**
- Les administrations exigent des **logiciels à jour et pris en charge** pour les systèmes sensibles

*Pourtant, Flock Safety continue de déployer et de vendre des caméras dont les logiciels ne sont plus pris en charge par leur fournisseur, qui ne reçoivent aucun correctif de sécurité, contiennent des centaines d'exploits connus et traitent des données sensibles des forces de l'ordre.*

### Pourquoi c'est important

L'utilisation de **logiciels en fin de vie** sur des appareils de surveillance signifie que :
- **Toute vulnérabilité publiée d'Android 8.x** fonctionne sur ces caméras
- Du **code d'exploitation est disponible au public** pour de nombreuses vulnérabilités
- **Aucun correctif ne viendra corriger** les nouveaux problèmes découverts
- La **conformité réglementaire** (FISMA, NIST, CMMC) est impossible à atteindre

______

## Vulnérabilité critique no 3 : absence de chiffrement à l'exécution

### CVE-2025-47824 et CVE-2025-59407

**Gravité** : ÉLEVÉE à CRITIQUE (CVSS 2.0 à 9.8)

### Les affirmations de Flock Safety face à la réalité

**Le site Web de Flock Safety affirme** :
> « Les données et les vidéos sont chiffrées tout au long de leur cycle de vie. »

**Les recherches indépendantes de GainSec et de Ben Jordan concluent** :
> « Dans toutes nos recherches, nous n'avons rien déchiffré ni cassé. Tout était non chiffré à l'exécution. »

*L'écart entre l'affirmation commerciale et la réalité technique est total.*

### Données non chiffrées

Lorsqu'ils ont examiné les appareils, les chercheurs ont trouvé les éléments suivants **non chiffrés** :
1. **Les vidéos et images stockées**
2. **Les données de plaques d'immatriculation et leurs métadonnées**
3. **Les identifiants Wi-Fi et les clés API**
4. **Les fichiers de bases de données contenant les détections**
5. **Le trafic réseau** (voir la vulnérabilité no 6)
6. **Les journaux système contenant des informations sensibles**

### Contradiction sur la durée de conservation des données

**Affirmation de Flock Safety** : les données sont supprimées automatiquement après sept jours.  
**Résultat des recherches** : des images remontant à la **fabrication de l'appareil** (plusieurs mois ou années auparavant) ont été retrouvées.

Extrait du livre blanc de GainSec :
> « Nous avons trouvé des images datant de plus de sept jours. En fait, certaines images stockées avaient été prises lorsque la caméra s'est déclenchée dans l'usine où l'appareil a été fabriqué. »

*Cela signifie que les politiques de confidentialité annoncées ne sont pas appliquées sur l'appareil.*

### Conséquences pour la vie privée

Cette défaillance du chiffrement signifie que :
- **Le vol physique de l'appareil** entraîne une fuite immédiate des données
- **L'interception réseau** expose les données en clair
- Les **menaces internes** peuvent facilement exfiltrer des données
- Les **protections liées aux mandats de perquisition** peuvent ne pas s'appliquer aux données non chiffrées
- Il y a **violation de nombreuses réglementations** (HIPAA, CCPA, etc.)

______

## Vulnérabilité critique no 4 : identifiants codés en dur dans tout le système {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 et CVE-2025-59409

**Gravité** : CRITIQUE (CVSS 9.8 au maximum)

### Catégories de secrets codés en dur

Les chercheurs en sécurité ont découvert de **nombreux identifiants codés en dur** :

#### 1. Mots de passe des points d'accès Wi-Fi
- **Mot de passe universel** sur toutes les caméras Falcon/Sparrow
- **Impossible à modifier** par les utilisateurs ou les administrateurs
- **Connu des chercheurs** et publié dans le livre blanc (certaines parties sont expurgées)
- **Confirmé par CVE-2025-59409** : les micrologiciels de production Falcon et Sparrow (compilation `OPM1.171019.026`) sont livrés avec des **identifiants Wi-Fi de développement en clair**

#### 2. Clés API et jetons
- **Codés en dur dans le micrologiciel** et le code des applications
- **Donnent accès** aux services principaux
- **Découverts par rétro-ingénierie** des APK Android
- **Confirmés par l'image de septembre 2026** : une clé API du serveur principal est codée en dur dans `CameraSettings`, dans `com.flocksafety.android.common.lib`, une bibliothèque partagée intégrée à **toutes les 19 applications Flock** de l'appareil
- **L'identifiant et le secret client Auth0 sont stockés sur la partition `/persist` non chiffrée** à l'emplacement `flock/auth0/auth0_cred`, conçu pour survivre à une réinitialisation d'usine
- **Les identifiants renvoyés sont stockés en clair** après l'authentification de la caméra auprès du service Okta Auth0 de Flock avec sa propre adresse MAC

#### 3. Identifiants de bases de données
- **Bases SQLite** sans protection par mot de passe
- Identifiants **MySQL/PostgreSQL** dans des fichiers de configuration
- **Accès direct à la base de données** depuis un shell local

#### 4. Magasins de clés cryptographiques
- **Confirmé par CVE-2025-59407** : l'application DetectionProcessing intègre un magasin de clés Java et son mot de passe codé en dur. Ce magasin contient une **clé privée**
- **Gravité** : CRITIQUE (CVSS 9.8), car le matériel cryptographique est livré avec le binaire censé le protéger

#### 5. Noms de réseaux Wi-Fi
- **Liste des réseaux préférés** codée en dur dans le micrologiciel
- Permet des attaques par **point d'accès malveillant** (voir la vulnérabilité no 6)

#### 6. Identifiants de services cloud
- Jetons **AWS/Azure** intégrés au code
- **Clés API de services tiers** (ArcGIS, services de cartographie)
- Jetons **OAuth jamais renouvelés**

### Scénario d'attaque : réseau malveillant

À partir des noms de réseaux Wi-Fi codés en dur, les chercheurs ont démontré les étapes suivantes :

1. L'attaquant crée un **faux réseau Wi-Fi** dont le SSID correspond au nom codé en dur
2. La caméra **s'y connecte automatiquement** (les réseaux codés en dur sont prioritaires)
3. L'attaquant capture **tout le trafic réseau** par une attaque de l'homme du milieu
4. Les identifiants en clair sont extraits du trafic
5. L'attaquant obtient **l'accès au système principal**

**Aucun accès physique à la caméra n'est nécessaire.** Il suffit de se trouver à portée du Wi-Fi.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Schéma présentant cinq vecteurs d'attaque par identifiants codés en dur dans les caméras Flock Safety : mots de passe Wi-Fi, clés API, identifiants de bases de données et jetons de services cloud" >}}

______

## Vulnérabilité critique no 5 : absence d'authentification multifacteur

### Défaillance de la politique organisationnelle

**Gravité** : ÉLEVÉE (organisationnelle)

### La révélation

**Flock Safety n'exige pas l'authentification à deux facteurs ou multifacteur** pour certains services des forces de l'ordre. *Ce sont ces mêmes services qui consultent chaque jour les données de suivi de 150 millions de véhicules.*

Citation d'un chercheur en sécurité :
> « Quand j'ai appris cela, je n'en ai tout simplement pas cru mes oreilles. La procédure de sécurité lors de la connexion à Disney Plus serait trop contraignante pour certains services de police lorsqu'ils accèdent à des informations confidentielles et à la localisation, parfois, de pratiquement tout le monde. »

### Pourquoi c'est important

Sans authentification multifacteur :
- **Un seul mot de passe compromis** donne accès au système entier
- Les **attaques par hameçonnage** sont très efficaces
- La **réutilisation automatisée d'identifiants** issus d'autres fuites fonctionne
- Les **menaces internes** sont plus faciles à mettre à exécution
- Les **appareils volés** donnent un accès immédiat

### Comparaison

Exigences de sécurité pour des systèmes **moins sensibles** :
- **Disney+** : authentification à deux facteurs disponible
- **Gmail** : authentification à deux facteurs activée par défaut pour les nouveaux comptes
- **Services bancaires** : authentification à deux facteurs exigée par la loi
- **Réseaux sociaux** : l'authentification à deux facteurs est standard

Exigences de sécurité pour le **suivi quotidien de plus de 150 millions de véhicules** :
- **Flock Safety** : authentification à deux facteurs facultative (certaines agences ne l'utilisent pas)

### Réponse d'un sénateur américain

Cette découverte est expressément mentionnée dans **la lettre du sénateur Wyden** demandant une enquête de la FTC. Elle y est citée comme preuve que Flock Safety a :
> « inutilement exposé les données personnelles sensibles des Américains au vol par des pirates informatiques et des espions étrangers »

### Solution simple

Les **clés de sécurité USB/NFC** coûtent **10 à 25 dollars** et offrent :
- Une authentification **résistante à l'hameçonnage**
- **Aucune application ni aucun code** supplémentaire
- La conformité aux normes **FIDO2/WebAuthn**
- Une **expérience simple** (brancher la clé ou la toucher)

*Si cela représente « trop de complications » pour les forces de l'ordre, elles **ne devraient pas avoir accès** aux systèmes nationaux de surveillance.*

______

## Vulnérabilité critique no 6 : trafic réseau en clair

### Identifiant en attente d'attribution

**Gravité** : ÉLEVÉE (CVSS 7.8 selon l'estimation des chercheurs)

**Aucun identifiant CVE n'a été attribué à cette catégorie.** Le dossier attribué le plus proche, CVE-2025-59406, porte la classification CWE-319 relative à la transmission en clair, mais concerne un secret Auth0 intégré et non l'interception en transit. Les constats de cette section reposent toujours sur les rapports des chercheurs cités plus haut.

### La vulnérabilité

Lorsque les caméras se connectent à un réseau (LTE ou Wi-Fi), elles transmettent des données **sans chiffrement adéquat** :

**Trafic concerné** :
- Images et texte des plaques d'immatriculation
- Métadonnées de détection
- Journaux système
- Données de configuration
- Identifiants (dans certains cas)

### Vecteur d'attaque no 1 : réseau Wi-Fi malveillant

Les chercheurs ont démontré les étapes suivantes :
1. Retirer la carte SIM de la caméra **OU** créer un faux réseau correspondant au SSID codé en dur
2. La caméra se connecte au réseau Wi-Fi malveillant
3. Capturer le trafic avec **Wireshark** ou un analyseur de paquets similaire
4. L'analyser avec des outils tels que **NetworkMiner** ou **Unblo**
5. Extraire les **identifiants en clair** et les données sensibles

Citation des recherches de GainSec :
> « J'ai capturé pendant un moment les paquets transmis par l'une de ces caméras, puis je les ai analysés avec Wireshark et Unblo... et, bien sûr, les données contenaient des identifiants en clair. »

### Vecteur d'attaque no 2 : intercepteur IMSI / Stingray

Une attaque plus sophistiquée ne nécessite pas de proximité physique :
1. Utiliser un **intercepteur IMSI** (appareil Stingray artisanal) ou un SDR professionnel
2. **Détourner la connexion LTE** en se faisant passer pour une antenne-relais
3. La caméra se connecte à une **station de base malveillante**
4. **Intercepter tout le trafic** par une attaque de l'homme du milieu
5. Extraire les identifiants, les images et les métadonnées

**Aucun accès physique n'est nécessaire.** L'attaque fonctionne à **plusieurs centaines de pieds**.

### Possibilités d'attaque Tempest moderne

La transmission en clair permet aussi des **attaques de type Tempest**, dans lesquelles :
- Les émissions RF de la caméra peuvent être captées
- Le flux vidéo peut être **reconstitué à distance**
- La technique s'apparente aux méthodes de la **CIA durant la guerre froide**
- Les équipements SDR modernes rendent la méthode **accessible aux amateurs**

______

## Vulnérabilité critique no 7 : flux publics de caméras exposés

### Découverte de janvier 2026

**Gravité** : CRITIQUE (CVSS 10.0, exposition complète du système)

### La découverte

En janvier 2026, Ben Jordan et **404 Media** ont découvert qu'une simple **recherche Google** permettait de trouver :
- **Plus de 60 interfaces administratives Flock Safety complètement exposées**
- **Aucun nom d'utilisateur ni mot de passe requis**
- Des **flux vidéo en direct** et 30 jours d'archives
- **Accès complet au panneau de contrôle des caméras**

### Données accessibles

Depuis ces interfaces exposées, n'importe qui pouvait :
- **Regarder les flux vidéo en direct**
- **Consulter 30 jours** d'archives vidéo
- **Télécharger directement les fichiers vidéo**
- **Contrôler les caméras PTZ** (panoramique/inclinaison/zoom) des appareils Condor
- **Consulter les chemins d'accès et les empreintes** des preuves
- **Supprimer des preuves** d'un seul clic
- **Modifier les paramètres des caméras**
- **Voir les numéros de série et les emplacements des appareils**

### Atteintes à la vie privée observées

Ben Jordan a documenté les scènes suivantes :
- **Une famille installant un nourrisson dans une voiture** sur le parking d'un magasin Lowe's
- **Un homme quittant son domicile** à New York le matin
- **Une femme courant seule** sur un sentier forestier en Géorgie
- **Un couple se disputant** sur un marché de rue à Atlanta (l'IA a automatiquement zoomé sur les visages)
- **Un agent et une ambulance** intervenant lors d'une crise de santé mentale dans l'Iowa
- **Des enfants jouant** dans un terrain de jeu de la région de la baie de San Francisco
- **Un homme sur une balançoire** dans un parc vide, en plein moment privé

Citation de Ben Jordan :
> « Le simple fait de dire ces choses à voix haute me donne la nausée. Mais j'essaie de vous montrer une infime partie des informations auxquelles toute personne disposant d'un moteur de recherche commercial a eu accès au sujet de quiconque s'est rendu sur ce marché ou a marché sur ce sentier au cours des 31 derniers jours. »

### Capacités de ciblage

Les caméras Condor PTZ exposées disposent d'un **suivi assisté par IA** :
- **Zoom automatique** sur les personnes
- **Suivi des individus** en déplacement
- **Détection et ciblage** des téléphones (pour lire leur écran)
- **Suivi simultané de plusieurs cibles**
- **Enregistrement continu** sans supervision

### Risque de doxxing

Ben Jordan a montré à quelle vitesse une vidéo exposée permet d'identifier des personnes :
> « En moins de deux minutes de renseignement de source ouverte avec un moteur commercial de reconnaissance faciale, j'ai découvert que l'une de ces personnes venait de terminer ses études de médecine et que l'autre souffrait du syndrome du côlon irritable chronique. Le couple venait aussi d'avoir un bébé l'année dernière... J'ai également découvert qu'ils venaient de conduire plus de 45 minutes depuis leur domicile en banlieue. »

Le recoupement avec :
- Les services de **reconnaissance faciale**
- Les profils sur les **réseaux sociaux**
- Les bases de **données publiques**
- Les informations issues de **fuites de données** (Park Mobile, etc.)
- Les **journaux d'appels d'urgence** (publiés par de nombreuses villes)

Résultat : **désanonymisation complète en quelques minutes**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Schéma montrant comment des caméras Flock Safety PTZ exposées et leur suivi automatique par IA ont permis au public de consulter des vidéos en direct de personnes dans des parcs, sur des sentiers et dans des parkings" >}}

______

## Vulnérabilité critique no 8 : collecte de données non autorisée

### Contradiction avec les déclarations publiques

**Gravité** : ÉLEVÉE (conséquences sur la vie privée et juridiques)

### Affirmations de Flock Safety

**Déclaration du site officiel** :
> « Flock Safety ne capture ni n'enregistre les données des personnes, uniquement celles des véhicules. »

### Résultats des recherches indépendantes

**Ce que font réellement les caméras** :
1. **La détection de mouvement** déclenche la caméra **pour n'importe quel mouvement**, pas uniquement celui des véhicules
2. **L'IA cherche une plaque d'immatriculation** dans l'image
3. **Si aucune plaque n'est détectée**, l'image est tout de même **stockée**, et non supprimée
4. Un **dossier distinct** conserve les images sans plaque
5. Les **personnes, piétons et cyclistes** sont capturés et leurs images conservées

*L'affirmation selon laquelle les caméras ne traitent que les véhicules est fausse. La caméra stocke les images de toute personne qui passe devant elle.*

### Observations vérifiées

Les chercheurs ont documenté la capture d'images de :
- **Personnes marchant** devant une caméra (image conservée)
- **Mains faisant signe** devant l'objectif (image conservée)
- **Bureau ou objet déplacé** près de la caméra (image conservée)
- **Ouvriers d'usine** sur leur lieu de travail (images conservées pendant des mois)

Citation de GainSec :
> « Lorsque je suis passé devant la caméra, le module radar a déclenché le module caméra pour qu'il me photographie. Ensuite, l'IA embarquée a cherché une plaque d'immatriculation, n'en a pas trouvé, mais a tout de même stocké l'image dans un dossier distinct. »

### Conséquences juridiques

Cette collecte non autorisée de données pourrait :
- **Violer les politiques de confidentialité annoncées** (pratiques trompeuses)
- **Enfreindre des contrats d'achat** (si les villes ont spécifié « véhicules uniquement »)
- **Entraîner des violations du RGPD ou du CCPA** (citoyens de l'UE, résidents de Californie)
- **Invalider les accords de consentement**
- **Exposer l'entreprise à des poursuites** pour publicité mensongère

### Élargissement du champ de la surveillance

Les **caméras Condor PTZ** (déployées en 2025-2026) sont **explicitement conçues** pour suivre les personnes :
- **Détection des personnes par IA**
- **Zoom automatique** sur les visages
- **Suivi des déplacements**
- **Aucun mécanisme de retrait volontaire**
- **Souvent déployées** dans les parcs, sur les sentiers et dans les gares

*On passe ainsi massivement des « lecteurs de plaques d'immatriculation » à la surveillance générale de la population, sans modification des politiques, sans nouveaux contrats et sans avis public.*

______

## Vulnérabilité critique no 9 : ports USB exposés aux attaques Rubber Ducky

### Exploitation par accès physique

**Gravité** : ÉLEVÉE (en cas d'accès physique)

### La vulnérabilité

Les **boîtiers informatiques Bravo** et certains modèles de caméras disposent de :
- **Ports USB-C exposés** sur l'extérieur
- **Aucune protection physique** (joints du boîtier)
- **Exécution automatique** de périphériques USB
- **Aucune authentification requise**

### Attaque Rubber Ducky / BadUSB

Un **appareil BadUSB** (coût : 5 à 15 dollars) :
- Se fait passer pour un **clavier USB** auprès du système
- **Exécute des scripts préprogrammés** (charges utiles)
- **Fonctionne automatiquement** dès son branchement
- Ne nécessite **aucune interaction de l'utilisateur**

### Scénario d'attaque

GainSec a démontré les étapes suivantes :
1. S'approcher d'un appareil Flock déployé
2. Brancher un **appareil BadUSB** sur le port exposé
3. L'appareil exécute la charge utile (script)
4. La charge utile installe un **logiciel malveillant persistant**
5. L'attaquant **s'éloigne**
6. Le logiciel malveillant **rappelle son serveur de commande et de contrôle** par LTE/Wi-Fi

**Durée totale** : moins de 30 secondes

### Actions possibles avec les charges utiles

Les scripts automatisés peuvent :
- **Activer le point d'accès sans fil** (contourner les appuis sur le bouton)
- **Installer une porte dérobée** pour l'accès à distance
- **Exfiltrer des données** vers un serveur distant
- **Modifier les images ou les preuves**
- **Désactiver la caméra** ou provoquer un déni de service
- **Intégrer un botnet** pour lancer des attaques DDoS
- **Capturer les identifiants** d'autres systèmes

### Pourquoi c'est important

Avec **plus de 80 000 caméras**, souvent installées dans des **zones semi-rurales** avec **une visibilité limitée** :
- L'**accès physique** est relativement facile
- Il n'y a **ni gardes ni surveillance constante**
- Les appareils sont fixés avec de **simples colliers de serrage**
- Ils sont souvent installés à **sept pieds du sol** (accessibles avec un escabeau)

Citation de Ben Jordan :
> « Ces caméras ne sont pas exactement des forteresses impénétrables. Ce sont des caméras Android et des boîtiers informatiques en plastique, fixés à deux mètres du sol avec des colliers de serrage. »

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Schéma de la chaîne d'attaque montrant comment un appareil BadUSB branché au port USB exposé d'une caméra Flock Safety installe un logiciel malveillant persistant en moins de 30 secondes" >}}

______

## Vulnérabilité critique no 10 : clés API exposées au public

### Découverte par un chercheur en renseignement de sources ouvertes

**Gravité** : CRITIQUE (CVSS 9.5)

### La découverte

En 2025, le **chercheur OSINT Joshua Michael** a découvert :
- Un **site de démonstration Flock Safety exposé**, trouvé avec des requêtes Google ciblées
- **5 000 lignes de code source** visibles
- Une **clé API active** intégrée au code
- L'accès à **plus de 50 couches géospatiales privées**

### Accès accordé par la clé API

La **clé API ArcGIS** exposée donnait accès aux données suivantes :

**1. Données d'inscription**
- Noms des clients
- Adresses courriel
- Nombre de caméras par emplacement
- Possibilité de joindre des fichiers

**2. Emplacements en direct de voitures de patrouille** (plusieurs services)
- Suivi GPS en temps réel des véhicules de police
- Déploiement d'Aurora, dans le Colorado
- Police de Carrollton
- **Risque pour la sécurité nationale**

**3. Renseignements personnels sur les agents**
- Noms et numéros de téléphone
- Adresses courriel
- Zones de patrouille prévues
- Juridictions de rattachement

**4. Base de données des alertes de liste de surveillance** (Dallas, Texas)
- **6 000 enregistrements** de véhicules signalés
- Plaques d'immatriculation et motifs des signalements
- Lieux et horodatages des détections
- Identifiants des caméras ayant capturé les véhicules
- **Suivi des déplacements sur cinq mois**

Citation de Joshua Michael :
> « N'importe qui pouvait chercher sur Google, trouver cette carte et suivre les déplacements de ces personnes pendant cinq mois. Je précise aussi que la catégorie de motif comprend une personne simplement signalée comme “suspect”, et que beaucoup d'autres enregistrements n'indiquent aucun motif ou sont vides. »

### Surface d'attaque

Les clés API exposées permettent :
- **Le pistage de véhicules précis**
- De compromettre la **sécurité des agents** (domiciles, habitudes de patrouille)
- De compromettre la **sécurité opérationnelle** (lieux où se trouvent ou non les policiers)
- **L'intimidation de témoins** (suivre les personnes ayant signalé des crimes)
- La collecte de **renseignements criminels** par le crime organisé

### Contexte de la compromission : Flax Typhoon

Quelques semaines avant cette découverte, le groupe de pirates **parrainé par l'État chinois**, **Flax Typhoon**, a compromis ArcGIS, selon les chercheurs en sécurité Alexa Feminina et James Zhang.

Citation d'InfoSecurity Magazine :
> « Les pirates auraient ciblé une application ArcGIS légitime et accessible au public... utilisée pour le rétablissement après catastrophe, la gestion des urgences et d'autres fonctions essentielles. »

**Des États hostiles ont donc potentiellement eu accès** aux emplacements des véhicules de police, à l'identité des agents, aux emplacements des caméras de surveillance et aux habitudes d'intervention d'urgence.

______

## Vulnérabilités supplémentaires (résumé des plus de 50 failles)

### Vulnérabilités 11 à 51

Le livre blanc de GainSec documente **41 constats supplémentaires**, dont :

**Failles de conception système** :
- Mode de débogage activé dans les micrologiciels de production
- Processus de démarrage non sécurisé permettant de compromettre le chargeur de démarrage
- Aucun élément sécurisé ni TPM pour stocker les clés
- Mécanisme de mise à jour du micrologiciel prévisible

**Problèmes d'authentification** :
- Les jetons de session n'expirent jamais
- Aucune restriction d'accès fondée sur l'adresse IP
- Identifiants partagés entre plusieurs appareils
- Aucune épingle de certificat

**Sécurité réseau** :
- Ports ouverts avec des services de débogage
- Telnet activé sur certaines unités
- Serveurs FTP avec des identifiants faibles
- Vulnérabilités de rebinding DNS

**Vie privée et conservation des données** :
- Images stockées au-delà de la durée annoncée
- Métadonnées jamais supprimées
- Données de reconnaissance faciale collectées
- Suivi de lieux sans rapport avec des véhicules

**Sécurité physique** :
- Boîtiers faciles à démonter
- Interfaces série exposées
- Ports de débogage JTAG accessibles
- Aucun sceau révélant une tentative d'effraction

**Défaillances cryptographiques** :
- Génération de nombres aléatoires faible
- Clés de chiffrement codées en dur
- MD5 encore utilisé dans la chaîne de hachage
- Validation des certificats désactivée

**Divulgation d'informations** :
- Messages d'erreur détaillés révélant des éléments internes
- Affichage du contenu des répertoires activé sur les serveurs Web
- Identifiants présents dans les commentaires du code source
- Sauvegardes de configuration lisibles par tous

### État des CVE

En mai 2026 :
- **22 CVE attribuées** et publiées
- **8 CVE en attente** d'attribution par MITRE
- **21 constats** non soumis pour attribution de CVE, à la discrétion du chercheur
- **Tous les constats** sont documentés dans le livre blanc de GainSec

Détails techniques complets : [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## La réponse de Flock Safety

### Déclarations officielles

**Billet de blogue de novembre 2025** :
> « Flock s'engage à améliorer continuellement la sécurité... Aucune des vulnérabilités détaillées dans le rapport n'a d'incidence sur la capacité de nos clients à réaliser leurs objectifs de sécurité publique. »

**Affirmation** : l'exploitation des vulnérabilités exige un accès physique et une « connaissance approfondie ».

**Éléments contraires** :
- Les flux de caméras exposés ne nécessitaient **qu'une recherche Google**
- Les exploits sans fil ne nécessitent **qu'une proximité physique**
- L'exposition de la clé API était **entièrement à distance**
- Les mots de passe codés en dur sont **connus de tous** depuis leur divulgation

### Rejet des appareils de recherche

Flock a d'abord affirmé que les appareils de recherche étaient :
> « Non connectés au cloud... comme un iPhone volé dans un camion avant sa première connexion. »

*Cette affirmation s'est révélée fausse.* Les chercheurs ont testé des **appareils connectés au cloud** et obtenu les mêmes résultats. Les caméras accessibles au public présentaient les **mêmes vulnérabilités**, et 404 Media a découvert **plus de 60 caméras de production exposées**.

### Réponse envers les chercheurs

GainSec a indiqué que ses tentatives de divulgation responsable avaient entraîné :
- Une **offre de prime aux bogues assortie d'un accord de confidentialité** (qui aurait empêché la divulgation)
- **Aucune confirmation** des correctifs
- Une **déclaration aux médias** publiée avant la fin du délai de 90 jours
- **Aucune mention du chercheur** dans la déclaration publique
- La **perte de son emploi** dans les 48 heures suivant la publication de la vidéo

Ben Jordan a signalé :
- Des **visites de la police** à son domicile
- Des personnes qu'il soupçonnait d'être des **enquêteurs privés** photographiant sa maison
- Du **harcèlement par ses voisins**
- Des menaces de **mise en demeure** de la part de Flock Safety

Citation de Ben :
> « Je ne considère pas ces événements comme les conséquences ou les sanctions de mes recherches sur les vulnérabilités de sécurité. Je les considère comme les conséquences et les sanctions de ma démarche éthique et transparente. »

### Déploiement continu

*Malgré tout cela*, Flock Safety :
- **Continue de vendre** des appareils vulnérables
- N'a publié **aucune mise à jour de micrologiciel** corrigeant les causes profondes
- Utilise **toujours Android Things 8.x** (fin de vie en 2021)
- N'impose **aucune authentification multifacteur** aux forces de l'ordre

______

## Réponses législatives et politiques

### Demande d'enquête du Sénat américain

**Février 2026** : les sénateurs **Ron Wyden** (Oregon) et **Raja Krishnamoorthi** (Illinois) ont envoyé une lettre officielle à la FTC pour demander une enquête.

**Extrait de la lettre** :
> « Flock a inutilement exposé les données personnelles sensibles des Américains au vol par des pirates informatiques et des espions étrangers. »

**Motifs cités** :
- Risques pour la sécurité nationale
- Déclarations trompeuses sur la confidentialité
- Pratiques de sécurité inadéquates
- Absence d'obligation d'utiliser l'authentification multifacteur

### Décisions de conseils municipaux

**Denver, Colorado** :
- En décembre 2025, le conseil municipal a **voté contre** le renouvellement du contrat avec Flock
- Il a dénoncé le **« mépris de Flock pour l'honnêteté et la responsabilité »**
- En janvier 2026, le maire a **passé outre la décision** au moyen d'un « accord conclu en coulisses »
- La controverse publique se poursuit

**Evanston, Illinois** :
- La ville a découvert que **l'ICE utilisait les caméras** sans son consentement
- Elle a voté le **retrait des caméras**
- *Flock a réinstallé les caméras sans autorisation*
- La ville utilise l'argent des contribuables pour **recouvrir les caméras** et engager des poursuites

**Oakland, Californie** :
- Le vote sur une **extension de 2,25 millions de dollars** a été reporté
- Un audit de sécurité indépendant a été commandé
- L'audit a jugé **trompeuses** les affirmations de Flock sur l'efficacité de son système

### Demandes de documents publics

Plusieurs villes mènent des enquêtes en s'appuyant sur :
- Des recherches en sécurité accessibles au public
- Des demandes fondées sur la FOIA concernant les contrats de Flock
- Des exigences d'audit indépendant
- Les pressions exercées par les communautés et les groupes de défense

______

## Analyse technique : scénarios d'attaque réels

### Scénario 1 : surveillance par un État-nation

**Acteur de la menace** : service de renseignement étranger

**Objectif** : suivre des responsables gouvernementaux

**Méthode** :
1. Utiliser un intercepteur IMSI pour intercepter le trafic LTE des caméras
2. Extraire du flux les identifiants en clair
3. Accéder au serveur principal avec des clés API compromises (ou à une couche ArcGIS exposée précédemment)
4. Interroger la base de données pour trouver les véhicules immatriculés auprès d'organismes publics
5. Suivre les déplacements de responsables et de militaires

**Délai d'exécution** : plusieurs jours (une fois l'infrastructure en place)  
**Probabilité de détection** : faible (le canal C2 chiffré ressemble à du trafic légitime)

### Scénario 2 : contre-surveillance par le crime organisé

**Acteur de la menace** : organisation de trafic de drogue

**Objectif** : repérer les habitudes de patrouille de la police

**Méthode** :
1. Acheter un appareil BadUSB (15 dollars)
2. Conduire jusqu'aux caméras présentes sur le territoire d'opération
3. Brancher l'appareil BadUSB au port USB exposé (30 secondes)
4. La charge utile désactive la caméra ou modifie les images
5. Autre option : la charge utile exfiltre le suivi des véhicules de police vers un serveur distant

**Délai d'exécution** : 30 secondes par caméra  
**Probabilité de détection** : faible (l'activité ressemble à celle d'un périphérique légitime)

### Scénario 3 : harcèlement et violence conjugale

**Acteur de la menace** : ancien partenaire violent

**Objectif** : suivre les déplacements de la victime

**Méthode** :
1. Obtenir la plaque d'immatriculation de la victime (information publique)
2. Chercher sur Google une interface de caméra Flock exposée (vulnérabilité découverte en janvier 2026)
3. Interroger 30 jours d'images pour trouver les apparitions du véhicule
4. Recouper ces données avec des bases publiques (adresse professionnelle, domicile, etc.)
5. Établir les habitudes et les horaires de la victime

**Délai d'exécution** : de quelques minutes à quelques heures  
**Probabilité de détection** : nulle (aucun journal d'authentification n'existe)

### Scénario 4 : falsification de preuves

**Acteur de la menace** : accusé dans une affaire pénale

**Objectif** : détruire des preuves avant le procès

**Méthode** :
1. Découvrir l'emplacement de la caméra lors de la communication des éléments du mandat
2. Accéder physiquement à la caméra (séquence d'appuis sur le bouton)
3. Obtenir un shell root
4. Parcourir le dossier des preuves
5. Supprimer des images ou vidéos précises, ou modifier leurs horodatages

**Délai d'exécution** : moins de cinq minutes  
**Probabilité de détection** : faible (sauf si la caméra est examinée en criminalistique avant l'accès de la défense)

### Scénario 5 : militant pour la vie privée ou journaliste

**Acteur de la menace** : défenseur de la transparence

**Objectif** : documenter les excès de la surveillance

**Méthode** :
1. Utiliser des appareils de détection (voir notre [guide matériel Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Cartographier l'emplacement des caméras dans la communauté
3. Déposer des demandes FOIA sur les politiques de gestion des images
4. Démontrer les vulnérabilités au conseil municipal
5. Demander le retrait des appareils ou la mise en place d'un contrôle

**Délai d'exécution** : continu  
**Probabilité de détection** : élevée (activité publique)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrice comparant cinq scénarios d'attaque réels contre les caméras Flock Safety : surveillance par un État-nation, contre-surveillance du crime organisé, harcèlement, falsification de preuves et défense de la vie privée" >}}

______

## Se protéger contre ces vulnérabilités

### Pour les services des forces de l'ordre

**Mesures immédiates** :
1. **Exiger l'authentification multifacteur ou à deux facteurs** pour tous les utilisateurs (clés de sécurité USB)
2. **Vérifier chaque mois les journaux d'accès** pour repérer les recherches non autorisées
3. **Limiter le partage** aux juridictions qui en ont réellement besoin
4. **Isoler le réseau** : placer les caméras sur des VLAN dédiés
5. **Sécuriser physiquement les appareils** : sceaux révélateurs d'effraction et surveillance des caméras
6. Préparer un **plan de réponse aux incidents** en cas de compromission

**Exigences contractuelles** :
1. **Audits de sécurité réguliers** par des entreprises indépendantes
2. **Mises à jour obligatoires du micrologiciel** dans les 30 jours suivant la publication d'un correctif
3. **Notification des CVE** dans les 24 heures
4. **Stockage chiffré des preuves** avec des clés gérées par le client
5. **Pénalités prévues dans les accords de niveau de service** en cas de faille de sécurité
6. **Droit d'audit** des installations et du code du fournisseur

**Stratégie à long terme** :
1. Prévoir la **migration hors des systèmes d'exploitation en fin de vie**
2. Utiliser une **infrastructure auto-hébergée** (réduire la dépendance au cloud)
3. Évaluer les **solutions libres**
4. Faire preuve de **transparence envers la communauté** sur l'emplacement des caméras et les politiques en vigueur

### Pour Flock Safety (recommandations)

**Priorité critique** (immédiate) :
1. **Désactiver** la création d'un point d'accès sans fil par appui sur le bouton
2. **Imposer l'authentification multifacteur** à tous les comptes (sans exception)
3. **Renouveler tous les identifiants codés en dur** sur l'ensemble du système
4. Publier un **correctif d'urgence** pour les interfaces publiques exposées
5. Chiffrer les données **au repos** et gérer correctement les clés

**Priorité élevée** (30 jours) :
1. **Migrer vers un système d'exploitation pris en charge** (Android 12 ou ultérieur, ou Linux)
2. Créer un **programme de prime aux bogues sans accord de confidentialité**
3. **Publier les résultats d'un audit de sécurité indépendant**
4. Chiffrer **de bout en bout le trafic réseau**
5. **Améliorer la sécurité physique** (retirer les ports USB exposés, renforcer les boîtiers)

**Priorité moyenne** (90 jours) :
1. **Reconcevoir complètement** le système d'authentification
2. Mettre en place un **démarrage sécurisé** avec micrologiciel vérifié
3. Intégrer un **module matériel de sécurité**
4. Obtenir des **certifications de conformité** (FedRAMP, SOC 2, ISO 27001)
5. Fournir aux clients un **tableau de bord de sécurité** avec des notifications de fuite

**Long terme** (un an) :
1. Publier en **logiciel libre des composants de sécurité** (pour établir la confiance)
2. Créer un programme de **tests adversariaux** (équipe rouge)
3. Définir des exigences pour les **postes en ingénierie de la sécurité**
4. Intégrer des pratiques de sécurité au **cycle de développement logiciel** (DevSecOps)
5. Participer à l'élaboration des **normes du secteur** (OWASP, CIS)

### Pour les particuliers

**Moyens de protection** :
1. **Utiliser des appareils de détection** (voir notre [guide matériel](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Cartographier l'emplacement des caméras** dans votre secteur
3. **Varier les itinéraires et les horaires** pour réduire l'analyse des habitudes
4. **Demander au conseil municipal** davantage de contrôle et de transparence
5. **Déposer une demande FOIA** concernant vos données (lorsque la loi le permet)
6. **Soutenir les lois sur la vie privée** aux niveaux de l'État et fédéral

**Mesures de sécurité opérationnelle** :
1. **Éviter les véhicules distinctifs** (choisir une marque, un modèle et une couleur courants)
2. **Utiliser d'autres véhicules** pour des activités sensibles (lorsque la loi le permet)
3. **Choisir d'autres moyens de transport** (vélo, transports publics, marche)
4. **Utiliser des caches de plaque d'immatriculation protégeant la vie privée** (uniquement si la loi locale l'autorise)
5. **Utiliser des pochettes de Faraday** pour les téléphones si le risque de corrélation est préoccupant

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Feuille de route priorisée des corrections que Flock Safety devrait mettre en œuvre immédiatement, sous 30 jours, sous 90 jours et à long terme pour corriger les vulnérabilités critiques" >}}

______

## L'équipe de recherche

### GainSec (Jon « GainSec » Gaines)

**Parcours** : professionnel de la sécurité offensive, plus de dix ans d'expérience

**Contributions** :
- A découvert **47 des 51** vulnérabilités
- A publié un **livre blanc officiel** contenant les détails techniques
- A coordonné la **divulgation responsable** avec Flock Safety
- A enregistré **30 CVE** (22 publiées, 8 en attente)
- A créé une **liste de vérification pour les défenseurs** à l'intention des professionnels de la sécurité

**Contact** : whitepaper@gainsecmail.com  
**Recherche** : [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)  
**Blogue** : [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Parcours** : journaliste, musicien et enquêteur en technologies

**Contributions** :
- A **documenté les vulnérabilités en vidéo**
- A réalisé des **démonstrations publiques** pour les journalistes (The Guardian, 404 Media)
- A découvert **plus de 60 flux de caméras exposés** par une recherche Google
- A mené des **actions de sensibilisation et d'éducation du public**
- A **coordonné les démarches législatives** auprès de bureaux de sénateurs

**Contact** : par sa chaîne YouTube  
**Travaux** : YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Parcours** : spécialiste OSINT et chercheur en protection de la vie privée

**Contributions** :
- A découvert des **clés API exposées** à l'aide de recherches Google ciblées
- A documenté les **couches ArcGIS exposées**
- A mis en œuvre une **méthodologie OSINT** pour le suivi des recherches
- A **recoupé des données avec des fuites publiques**

**Organisation** : Next AI, cabinet de renseignement toutes sources

### Contributeurs

- **404 Media** : journalisme d'enquête et divulgation publique
- **The Guardian** : couverture internationale
- **Lucy Parsons Labs** : plusieurs années de sensibilisation et de recherche sur l'ALPR
- **Sassy South** : mobilisation communautaire et transparence
- **DeFlock / Will Freeman** : projet de cartographie des caméras
- **Ed Vogel** : analyse juridique et politique

______

## Considérations éthiques

### Calendrier de divulgation responsable

La communauté de la sécurité a suivi les bonnes pratiques de **divulgation responsable** :

**Procédure habituelle** :
1. Découvrir une vulnérabilité
2. **Notifier le fournisseur en privé pendant 90 jours**
3. Le fournisseur développe et déploie un correctif
4. Procéder à la **divulgation publique** après le correctif ou au bout de 90 jours (selon la première éventualité)
5. Publier une analyse détaillée pour favoriser l'apprentissage défensif

**Déroulement réel** :
1. GainSec découvre des vulnérabilités (fin 2024)
2. **Contacts répétés** avec Flock Safety (à partir de février 2025)
3. Flock propose une **prime aux bogues avec accord de confidentialité** (pour réduire au silence)
4. Flock publie une **déclaration anticipée** dans la presse (sans citer le chercheur)
5. **Aucune confirmation** du déploiement des correctifs
6. GainSec procède à la **divulgation publique** après l'expiration des périodes de 90 jours
7. Ben Jordan et 404 Media **vérifient indépendamment** les failles sur des systèmes de production

### Représailles contre les chercheurs

GainSec et Ben Jordan ont tous deux signalé :
- Une **perte d'emploi** ou des difficultés professionnelles
- Des **visites de la police** à leur domicile
- Une **surveillance présumée** de leur maison et de leurs biens
- Du **harcèlement par les voisins**
- Des **menaces de mise en demeure**
- Des **attaques sur les réseaux sociaux** (le PDG de Flock les a qualifiés de « terroristes »)

Cet **effet dissuasif** sur la recherche en sécurité :
- Décourage la divulgation des vulnérabilités
- Retarde les correctifs de sécurité critiques
- Nuit à la sécurité publique
- Va à l'encontre des normes éthiques de la communauté de la sécurité

*La réaction de Flock Safety envers les chercheurs qui ont suivi les procédures de divulgation établit un précédent dangereux pour toute la communauté de la recherche en sécurité.*

Citation de Ben Jordan :
> « Je n'ai pas les moyens de consacrer encore plusieurs mois à une autre vulnérabilité de Flock Safety. Comme vous pouvez le constater, celle-ci est urgente et, franchement, je crains qu'elle ne soit déjà exploitée. »

### Intérêt public

Ces chercheurs ont agi **dans l'intérêt public** en :
- **Suivant les procédures de divulgation responsable**
- **Informant le fournisseur en premier** avant toute divulgation publique
- **Expurgeant les détails sensibles** qui faciliteraient une exploitation
- **Fournissant des conseils défensifs** aux professionnels
- **Demandant des changements de politique** par les voies appropriées
- **Acceptant des risques personnels** pour informer le public

Sans leur travail :
- **Plus de 80 000 caméras vulnérables** resteraient sans correction
- **Plus de 150 millions d'analyses quotidiennes de véhicules** resteraient sans protection
- **Des millions d'Américains** resteraient exposés sans le savoir
- La **sécurité nationale** serait compromise
- **Aucune mesure législative** ne serait en cours

______

## Conclusion : la voie à suivre

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Chronologie du processus de divulgation des vulnérabilités de Flock Safety de 2024 à 2026, de la découverte initiale à la divulgation responsable, en passant par l'exposition toujours non corrigée" >}}

### Situation actuelle (mai 2026)

- **Plus de 50 vulnérabilités critiques** documentées et partiellement divulguées
- **Plus de 80 000 caméras** restent déployées avec des failles non corrigées
- Le fournisseur n'a mis en œuvre **aucune correction complète**
- **Mesures réglementaires limitées** (enquête demandée à la FTC, mais non ouverte)
- **Risque d'exploitation persistant** pour la sécurité nationale et la vie privée

### Mesures nécessaires

**Dans tout le secteur** :
1. **Audits de sécurité obligatoires** avant tout déploiement gouvernemental
2. **Tests indépendants** par des tiers qualifiés
3. **Publication des résultats d'audit**
4. **Responsabilité des fournisseurs** en cas de défaillance de sécurité
5. **Conformité aux normes** (NIST, ISO, etc.)

**Pour Flock Safety en particulier** :
1. **Correctifs d'urgence immédiats** pour les vulnérabilités critiques
2. **Migration du système d'exploitation** vers une plateforme prise en charge
3. **Reconnaissance publique de l'ampleur du problème**
4. **Dédommagement des chercheurs touchés**
5. **Rapports transparents** sur la posture de sécurité

**Pour les forces de l'ordre** :
1. Inclure des **exigences de sécurité dans les contrats d'achat**
2. Effectuer des **audits réguliers** des systèmes déployés
3. Rendre l'**authentification multifacteur obligatoire** pour tous les utilisateurs
4. Préparer des **plans de réponse aux incidents**
5. Assurer la **transparence envers la communauté** sur les programmes de surveillance

**Pour les législateurs** :
1. Établir des **normes fédérales** pour les technologies de surveillance
2. Exiger la **notification des vulnérabilités aux parties touchées**
3. Protéger les **lanceurs d'alerte** et les chercheurs en sécurité
4. Prévoir des **recours civils** en cas d'atteinte à la vie privée
5. Créer des **organismes de contrôle** dotés d'une expertise technique

### Enjeux plus vastes

Cette étude de cas représente **bien plus que Flock Safety**. Elle illustre :
- Un **secteur de la surveillance** qui privilégie la croissance à la sécurité
- Des **achats publics** sans expertise technique suffisante
- Des **affirmations de fournisseurs** sans vérification ni remise en question
- Des **incitations financières** incompatibles avec la sécurité publique
- Des **lacunes réglementaires** dans la supervision des technologies émergentes

*Toute ville qui signe un contrat Flock sans vérification de sécurité indépendante accepte ces risques au nom de ses habitants.*

### Appel à l'action

**Professionnels de la sécurité** :
- **Soutenez la divulgation responsable**
- **Contribuez aux outils de sécurité libres**
- **Demandez la protection des chercheurs**

**Forces de l'ordre** :
- **Exigez des comptes aux fournisseurs**
- **Exigez des audits de sécurité avant le déploiement**
- **Imposez immédiatement l'authentification multifacteur**
- **Consultez la communauté de la sécurité**

**Décideurs politiques** :
- **Adoptez des lois imposant des normes de sécurité**
- **Financez des audits indépendants** des technologies de surveillance
- **Protégez les lanceurs d'alerte** et les chercheurs
- **Créez des organismes de contrôle** dotés d'une expertise technique

**Public** :
- **Informez-vous** sur la surveillance dans votre communauté
- **Assistez aux réunions du conseil municipal** lorsque des contrats sont examinés
- **Soutenez les organisations** qui défendent la transparence
- **Contactez vos représentants** pour leur faire part de vos préoccupations
- Utilisez des **outils de détection** pour cartographier la surveillance (voir notre [guide matériel](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### À lire aussi

- **[Vidéosurveillance par les caméras Flock Safety : déploiement, enjeux de confidentialité et moyens de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** : comprendre le paysage de la surveillance
- **[Projet de détection Flock-You : guide de matériel anti-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** : fabriquer son propre détecteur

Attendre que le secteur corrige ces failles ne protège personne. Les **[appareils de détection FlockYou](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** de STS Collective fonctionnent dès maintenant, et le code lecteur **SIMEONONSECURITY** donne jusqu'à 20 % de réduction.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acheter les détecteurs FlockYou, économiser 20 %
{{< /centerbutton >}}

______

## Références

1. [Recherche de GainSec sur l'écosystème anti-crime - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Livre blanc GainSec - DOI Zenodo : 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blogue GainSec - analyses techniques non officielles](https://gainsec.com/)
4. [Réponse officielle de Flock Safety - novembre 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - flux de caméras Flock exposés](https://www.404media.co/)
6. [Ben Jordan sur YouTube - démonstrations de vulnérabilités](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [Base de données CVE de MITRE](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - surveillance ALPR](https://www.eff.org/issues/automated-license-plate-readers)
10. [Lettre du sénateur Wyden à la FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - recherches sur l'ALPR](https://lucyparsonslabs.com/)
12. [Projet DeFlock - cartographie des caméras](https://deflockproject.org/)
13. [Distributed Denial of Secrets - images du système de fichiers d'une caméra ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - les caméras Flock présentent de nombreuses vulnérabilités de sécurité et identifiants codés en dur](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED et 404 Media - des pirates ont pénétré une caméra Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - cette semaine en sécurité : les caméras Flock sont anciennes](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905 : use-after-free du GPU Qualcomm Adreno](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568 : confusion de types dans les sockets du noyau Linux](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - détection ALPR Flock Safety et référence des appareils](https://wifimothership.com/flock)
20. [CVE.org - recherche dans les dossiers du programme CVE](https://www.cve.org/)
21. [Alerte de sécurité de Flock Safety - détection de coups de feu et lecteurs de plaques](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2 : exécution de code à distance sans fil sur Falcon et Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3 : shell root sur le boîtier informatique Bravo de Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
