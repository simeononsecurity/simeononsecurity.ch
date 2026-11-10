---
title: "Les types de cyberattaques les plus courants et leur détection"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Découvrez les cyberattaques les plus courantes, les traces qu'elles laissent dans les journaux et la télémétrie, et entraînez-vous à les détecter dans un laboratoire de sécurité à domicile."
genre: ["Cybersécurité", "Détection des menaces", "Blue Team", "Opérations de sécurité", "Développement de carrière"]
tags: ["types de cyberattaques", "logiciel malveillant", "rançongiciel", "hameçonnage", "spear phishing", "ingénierie sociale", "usurpation", "attaques basées sur l'identité", "credential stuffing", "password spraying", "injection SQL", "cross-site scripting", "attaque de la chaîne d'approvisionnement", "menace interne", "tunnel DNS", "attaques IoT", "attaques basées sur l'IA", "déni de service", "ingénierie de détection", "analyste SOC", "Blue Team", "laboratoire à domicile", "analyse des journaux", "réponse aux incidents", "MITRE ATT&CK", "carrière en cybersécurité", "recherche de menaces", "centre des opérations de sécurité", "télémétrie", "triage des alertes"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Illustration numérique sur fond sombre, avec des icônes abstraites et colorées représentant différents types de cyberattaques, comme les rançongiciels, le hameçonnage et le déni de service."
coverCaption: ""
---

Un **type d'attaque** désigne une catégorie de techniques, et non un outil unique. Les rançongiciels, le hameçonnage et le credential stuffing sont des méthodes qu'un adversaire répète contre de nombreuses cibles en apportant de légères variantes. Connaître ces catégories vous donne un répertoire mental des alertes que vous rencontrerez dans une équipe de sécurité.

*Les familles de logiciels malveillants apparaissent et disparaissent en quelques mois. Les catégories d'attaque ci-dessous restent stables depuis des années, et chacune laisse une trace reconnaissable dans la télémétrie des terminaux, des identités, du réseau ou de la messagerie.*

<!--more-->

## Points clés

- **Apprenez le schéma, pas la charge utile.** Les catégories d'attaque évoluent bien moins vite que les outils individuels.
- **Chaque catégorie laisse des traces.** La détection commence par l'identification de la télémétrie qui enregistre l'activité.
- **Reproduisez une attaque pour la comprendre.** Un laboratoire à domicile transforme une catégorie abstraite en observation enregistrée.
- **Consignez vos résultats.** Une courte note d'enquête prouve le travail accompli et explique les éléments recueillis.

## Les types d'attaque en un coup d'œil

Le tableau répertorie les catégories les plus fréquemment rencontrées par les équipes de sécurité. Les sections suivantes décrivent chaque catégorie, ses variantes courantes et les données qu'un défenseur examine pour la détecter.

| Type d'attaque | Effet |
|---|---|
| **Logiciel malveillant** | Exécute un logiciel nuisible, par exemple un rançongiciel, un logiciel espion ou un cheval de Troie |
| **Déni de service** | Inonde un service de trafic jusqu'à ce que les utilisateurs légitimes perdent l'accès |
| **Hameçonnage** | Trompe une personne pour qu'elle révèle ses identifiants ou exécute un fichier malveillant |
| **Usurpation** | Se fait passer pour un système, un expéditeur ou une adresse de confiance |
| **Attaques basées sur l'identité** | Abusent d'identifiants volés ou falsifiés pour agir comme un utilisateur légitime |
| **Injection de code** | Insère du code malveillant dans une application pour en modifier le comportement |
| **Attaques de la chaîne d'approvisionnement** | Compromettent un fournisseur, une bibliothèque ou un canal de mise à jour de confiance |
| **Ingénierie sociale** | Manipule une personne pour qu'elle agisse de manière dangereuse |
| **Menaces internes** | Détournent les accès d'un employé actuel ou ancien |
| **Tunnel DNS** | Encode des données dans des requêtes DNS afin de contourner les contrôles |
| **Attaques IoT** | Visent les appareils connectés pour se déplacer dans le réseau, espionner ou rejoindre un botnet |
| **Attaques basées sur l'IA** | Utilisent l'apprentissage automatique pour générer du contenu, usurper l'identité de personnes ou contourner des filtres |

**Remarque sur le périmètre :** ces catégories se chevauchent. Un e-mail d'hameçonnage transmet souvent un logiciel malveillant, et le vol d'identifiants précède souvent une attaque basée sur l'identité. Considérez la liste comme un ensemble de points de vue plutôt que comme des cases rigides.

______

## Logiciels malveillants

**Un logiciel malveillant** est un programme conçu pour nuire à un système, le contrôler ou en tirer profit. Le terme comprend les rançongiciels, les logiciels malveillants sans fichier, les logiciels espions et publicitaires, les chevaux de Troie, les vers, les rootkits, les enregistreurs de frappe et les botnets.

| Sous-type | Comportement |
|---|---|
| **Rançongiciel** | Chiffre des fichiers et exige un paiement pour fournir la clé de déchiffrement |
| **Logiciel malveillant sans fichier** | Utilise les outils système intégrés et écrit peu sur le disque |
| **Logiciel espion** | Collecte des données d'activité à l'insu de l'utilisateur |
| **Cheval de Troie** | Se fait passer pour un logiciel légitime afin d'être exécuté |
| **Ver** | Se copie d'un hôte à l'autre sans intervention de l'utilisateur |
| **Rootkit** | Se cache dans le système d'exploitation pour conserver un contrôle persistant |

**Où trouver les preuves :** les outils de détection et de réponse sur les terminaux, ou **EDR**, enregistrent les arbres de processus, les lignes de commande, les écritures de fichiers et les modifications du registre. Une attaque sans fichier produit aussi de la télémétrie sur les processus et les scripts, car le système d'exploitation lance toujours les outils qu'elle exploite.

______

## Déni de service

**Une attaque par déni de service (DoS)** inonde une cible de requêtes jusqu'à ce que les utilisateurs légitimes perdent l'accès. **Une attaque par déni de service distribué (DDoS)** répète la même méthode depuis de nombreux systèmes à la fois, ce qui rend le filtrage par adresse source beaucoup plus difficile.

| Caractéristique | DoS | DDoS |
|---|---|---|
| **Origine** | Un système | De nombreux systèmes |
| **Difficulté de blocage** | Modérée | Élevée, car les sources couvrent de nombreux réseaux |
| **Impact typique** | Perte de disponibilité | Perte de disponibilité à plus grande échelle |

**Où trouver les preuves :** le volume de trafic par rapport à une référence, le nombre de connexions par source, les pics du taux de requêtes et les changements du taux d'erreur. La surveillance de la disponibilité déclenche souvent une alerte avant que l'équipe de sécurité ne voie l'incident.

______

## Hameçonnage

**L'hameçonnage** utilise des e-mails, des SMS, des appels téléphoniques ou les réseaux sociaux pour inciter une personne à révéler ses identifiants ou à ouvrir une pièce jointe malveillante. Les variantes se distinguent par leur cible et leur canal.

| Variante | Cible et canal |
|---|---|
| **Spear phishing** | Une personne ou une équipe précise, généralement par e-mail |
| **Whaling** | Des cadres et dirigeants, souvent pour détourner de l'argent ou des données |
| **Smishing** | Des SMS frauduleux |
| **Vishing** | Des appels ou messages vocaux frauduleux |

**Où trouver les preuves :** les journaux de la passerelle de messagerie, les résultats d'analyse d'URL, l'analyse des pièces jointes et les signalements des utilisateurs. Le signalement d'un employé vigilant compte parmi les signaux les plus précieux de cette liste.

______

## Usurpation

**L'usurpation** dissimule un attaquant derrière une identité de confiance afin que la cible accepte la connexion, le message ou l'adresse. Le déguisement fait gagner du temps et contourne les contrôles fondés sur la confiance.

| Type | Élément falsifié |
|---|---|
| **Usurpation de domaine** | Un site ou un domaine de messagerie ressemblant à celui d'une marque réelle |
| **Usurpation d'adresse e-mail** | L'adresse d'expéditeur d'un message |
| **Usurpation ARP** | Une adresse réseau locale pour intercepter le trafic entre deux hôtes |

**Où trouver les preuves :** les résultats SPF, DKIM et DMARC dans les en-têtes de messages, l'ancienneté du domaine, les incohérences de certificats et les alertes d'adresse en double sur le réseau local.

______

## Attaques basées sur l'identité

**Les attaques basées sur l'identité** utilisent un compte valide au lieu d'une faille logicielle. L'attaquant dispose d'identifiants fonctionnels, donc son activité ressemble à un usage normal et se fond dans le bruit de fond. Cette catégorie est à l'origine d'une grande partie des alertes traitées chaque jour par un **centre des opérations de sécurité (SOC)**.

*Si vous ne pratiquez qu'une seule catégorie dans un laboratoire à domicile, choisissez celle-ci. Les signaux sont riches, les exercices sont reproductibles et la configuration reste modeste.*

| Technique | Déroulement |
|---|---|
| **Kerberoasting** | Demande un ticket de service, puis en casse le mot de passe chiffré hors ligne |
| **Attaque de l'homme du milieu (MITM)** | S'intercale entre deux parties pour lire ou modifier une session |
| **Pass-the-hash** | Réutilise un hachage de mot de passe volé pour ouvrir une nouvelle session |
| **Golden ticket** | Forge un ticket Kerberos pour obtenir un accès étendu au domaine |
| **Silver ticket** | Forge un ticket de service pour un service précis |
| **Collecte d'identifiants** | Rassemble en masse des noms d'utilisateur et des mots de passe |
| **Credential stuffing** | Réessaie un même ensemble d'identifiants sur de nombreux sites sans lien entre eux |
| **Password spraying** | Essaie un mot de passe courant sur de nombreux comptes |
| **Force brute** | Essaie de nombreux mots de passe contre un compte |
| **Rétrogradation** | Force une connexion à utiliser une version plus faible du protocole |

**Où trouver les preuves :** les enregistrements de connexion, le nombre d'échecs d'authentification, les anomalies de jetons, les alertes de déplacement impossible et les détections de risque d'identité. **L'hameçonnage adversary-in-the-middle (AiTM)** appartient aussi à cette catégorie, car l'attaquant vole un jeton de session actif plutôt qu'un mot de passe. La réutilisation du jeton depuis une infrastructure inconnue déclenche le moteur de risque d'identité.

______

## Injection de code

**L'injection de code** place du code contrôlé par l'attaquant dans une application vulnérable afin que celle-ci l'exécute dans le cadre de son fonctionnement normal. C'est l'application, et non l'attaquant, qui réalise l'action nuisible.

| Type | Cible |
|---|---|
| **Injection SQL** | Une requête de base de données construite à partir d'entrées non validées |
| **Cross-site scripting (XSS)** | Une page Web qui exécute le script de l'attaquant dans le navigateur d'un visiteur |
| **Malvertising** | Un espace publicitaire légitime rempli de code malveillant |
| **Empoisonnement des données** | Un jeu d'entraînement destiné à un modèle d'IA ou d'apprentissage automatique |

**Où trouver les preuves :** les journaux d'applications Web, les enregistrements de requêtes de base de données, les rapports de politique de sécurité du contenu et les requêtes qui diffèrent de l'utilisation normale de l'application.

______

## Attaques de la chaîne d'approvisionnement

**Une attaque de la chaîne d'approvisionnement** vise un tiers de confiance dont le produit ou le service atteint de nombreux clients. **Une attaque de la chaîne d'approvisionnement logicielle** injecte du code malveillant dans une application, une bibliothèque ou une mise à jour, puis le distribue à tous les utilisateurs du produit. **Une attaque de la chaîne d'approvisionnement matérielle** compromet un composant physique avant son expédition.

*Les logiciels modernes dépendent de bibliothèques tierces. Une seule dépendance compromise touche donc bien plus d'utilisateurs que le fournisseur initial.*

**Où trouver les preuves :** l'analyse de la composition logicielle, les enregistrements du pipeline de compilation, les connexions sortantes inattendues depuis une mise à jour de confiance et les contrôles d'intégrité des artefacts distribués.

______

## Ingénierie sociale

**L'ingénierie sociale** utilise la pression psychologique pour inciter une personne à agir de manière dangereuse. L'attaquant fait appel à l'autorité, l'urgence, la peur, l'argent ou la confiance.

| Technique | Approche |
|---|---|
| **Prétexte** | Invente une situation crédible pour gagner la confiance |
| **Compromission de messagerie professionnelle (BEC)** | Se fait passer pour un collègue de confiance afin de détourner un paiement ou d'obtenir des données |
| **Désinformation** | Diffuse de faux récits par les réseaux sociaux et les bots |
| **Quid pro quo** | Propose une récompense en échange d'informations ou d'un accès |
| **Piège sentimental** | Établit une fausse relation pour obtenir de l'argent, des données ou un accès |
| **Tailgating** | Suit un employé à travers une porte sécurisée |

**Où trouver les preuves :** les résultats d'authentification des e-mails, les demandes inhabituelles de changement de paiement, les dossiers du service d'assistance et les journaux d'accès physique.

______

## Menaces internes

**Une menace interne** est l'utilisation abusive des accès d'un employé actuel ou ancien, d'un prestataire ou d'un partenaire. Certaines personnes agissent délibérément, motivées par l'argent ou le ressentiment. D'autres sont négligentes, par exemple en laissant des identifiants dans un document partagé.

*Les rapports d'incident mentionnent plus souvent des personnes négligentes que des personnes malveillantes. Dans les deux cas, le même contrôle de détection s'applique : comparer l'accès à une référence définie pour le rôle.*

**Où trouver les preuves :** le volume des transferts de données, l'activité en dehors des heures habituelles, les changements de privilèges et les téléchargements massifs depuis des dépôts sensibles.

______

## Tunnel DNS

**Le tunnel DNS** encode des données dans les requêtes et réponses DNS. Presque tous les réseaux autorisent le DNS ; cette technique fait donc passer des données au-delà des contrôles conçus pour inspecter le trafic Web.

*La détection repose sur le volume et la forme. Un hôte qui envoie des milliers de requêtes à un seul domaine se distingue d'une référence normale, et des sous-domaines inhabituellement longs évoquent une charge utile encodée.*

**Où trouver les preuves :** les enregistrements de requêtes DNS, leur longueur et leur volume par hôte, les types d'enregistrement peu courants comme TXT et les recherches de domaines enregistrés quelques jours auparavant.

______

## Attaques contre les objets connectés

**Une attaque contre l'IoT** vise un appareil connecté comme une caméra, une imprimante, un thermostat ou un capteur. Les identifiants par défaut faibles et les mises à jour de micrologiciel rares font de ces appareils des points d'entrée fréquents. Une fois compromis, un appareil rejoint un botnet, divulgue des données ou sert de passerelle vers le réseau plus vaste.

*Le déploiement de la 5G multiplie les appareils connectés, et chaque nouvel appareil ajoute une cible dont le cycle de mise à jour est long.*

**Où trouver les preuves :** l'inventaire des appareils, les schémas de connexions sortantes, les transferts anormaux depuis un appareil à rôle fixe et les écarts de version du micrologiciel au sein d'un parc.

______

## Attaques basées sur l'IA

**Les attaques basées sur l'IA** appliquent l'apprentissage automatique aux activités de l'attaquant.

| Technique | Utilisation |
|---|---|
| **IA/ML adversarial** | Manipule les données d'entraînement ou les entrées pour tromper un modèle |
| **Dark AI** | Utilise l'IA et l'apprentissage automatique pour exploiter des vulnérabilités |
| **Deepfake** | Génère de faux contenus audio, vidéo ou images réalistes |
| **Ingénierie sociale générée par l'IA** | Mène à grande échelle des conversations convaincantes par chat ou par voix |

*Un appel vocal deepfake ou une conversation d'hameçonnage fluide renforce la crédibilité d'une vieille astuce. La technique de fond reste familière, ce qui explique pourquoi les compétences de détection fondées sur le comportement résistent mieux que celles liées à un seul outil.*

**Où trouver les preuves :** les signaux de provenance des contenus, une vérification par un autre canal pour les demandes d'argent ou d'accès et les anomalies comportementales liées aux changements d'identité et de paiement.

______

## Associer les attaques à la télémétrie

Chaque catégorie alimente une source de données différente. Le tableau les met en correspondance et vous donne un point de départ pour le travail de détection.

| Type d'attaque | Télémétrie principale |
|---|---|
| **Logiciel malveillant** | Enregistrements EDR des processus, fichiers et entrées du registre |
| **Déni de service** | Flux réseau et moniteurs de disponibilité |
| **Hameçonnage** | Journaux de passerelle de messagerie et d'analyse d'URL |
| **Usurpation** | Enregistrements d'authentification des e-mails et d'adresses réseau |
| **Basée sur l'identité** | Enregistrements de connexion et de protection des identités |
| **Injection de code** | Journaux d'applications Web et de requêtes de base de données |
| **Chaîne d'approvisionnement** | Pipeline de compilation et inventaire des dépendances |
| **Ingénierie sociale** | E-mails, service d'assistance et accès physiques |
| **Menace interne** | Enregistrements d'accès et de transfert des données |
| **Tunnel DNS** | Enregistrements de requêtes DNS |
| **IoT** | Inventaire des appareils et flux sortants |
| **Basée sur l'IA** | Enregistrements d'identité, de paiement et de provenance des contenus |

*Commencez le travail de détection par la colonne de télémétrie. Une règle utile part d'une source de données et d'un comportement connus, pas du nom d'un outil.*

**Les catégories se chevauchent pendant un incident.** Un message d'hameçonnage peut entraîner le vol d'identifiants, l'exécution de logiciels malveillants et une intrusion basée sur l'identité. Étiquetez la technique d'accès initial, puis consignez séparément les comportements qui suivent. Ainsi, un seul événement ne devient pas quatre alertes sans lien, et l'enquête bénéficie d'une chronologie plus claire.

______

## S'entraîner à les détecter en laboratoire

Une catégorie reste abstraite tant que vous ne l'avez pas observée. Un laboratoire à domicile permet de générer l'activité, de recueillir la télémétrie et de comparer une alerte à l'enregistrement brut. La [vidéo de carrière sur la création d'un centre des opérations de sécurité](https://www.youtube.com/watch?v=s3g8o7Np1_g) montre une configuration complète pour acquérir de l'expérience professionnelle avant l'embauche.

{{< youtube id="s3g8o7Np1_g" >}}

Commencez par la catégorie liée à l'identité. Créez un utilisateur de test, activez la journalisation des connexions et exécutez une série de connexions réussies et échouées. Lisez ensuite l'enregistrement et notez les champs qui distinguent l'usage normal de l'exercice.

**Un exercice reproductible :**

1. **Choisissez une catégorie** dans le tableau de télémétrie ci-dessus.
2. **Reproduisez une version inoffensive** de l'activité sur votre propre système ou compte de test.
3. **Collectez la télémétrie** produite par cette catégorie.
4. **Formulez l'idée de détection** sous forme de règle, de recherche enregistrée ou de requête.
5. **Testez la règle** avec l'exercice et vérifiez qu'elle se déclenche pour le comportement attendu.
6. **Consignez les limites** de la règle, y compris les activités qu'elle ne détecte pas.

Le [guide Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) détaille la création de l'environnement : licences, segmentation du réseau, collecte des journaux et tests de contrôle des identités. Le [guide Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) développe la même idée avec une configuration d'atelier comprenant un exercice d'attaque, de détection et de défense.

Pour utiliser un vocabulaire cohérent, associez le comportement observé à la technique correspondante de [MITRE ATT&CK](https://attack.mitre.org/). Considérez cette correspondance comme une aide pour l'analyste, et non comme une preuve d'attribution. Conservez l'événement brut, la requête, la version de la règle et ses angles morts connus avec le compte rendu de l'exercice.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Lire le guide Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Prochaines étapes

Commencez par une catégorie et un exercice. Ajoutez une deuxième catégorie après avoir terminé et documenté la première. L'objectif est d'approfondir une enquête, pas de créer une liste d'outils.

- **[Guide Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** construit l'environnement nécessaire à ces exercices.
- **[Créer un laboratoire informatique à domicile](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** décrit l'infrastructure sous-jacente à un laboratoire de sécurité.
- **[Conseils pour rédiger un CV informatique](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** montre comment présenter un laboratoire documenté comme une expérience pratique.
- **[Les cinq principaux vecteurs de cyberattaque et leurs mesures d'atténuation](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** réduit la liste aux vecteurs les plus fréquents.

**Sources :** les catégories d'attaque et leurs sous-types suivent l'[aperçu CrowdStrike des cyberattaques courantes](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) de Kurt Baker. Les liens vers les produits et les références renvoient à la documentation Microsoft.
