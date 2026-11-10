---
title: "Construire un homelab en 10 niveaux, de Pi-hole à l’IA locale"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Construisez un homelab en dix étapes pratiques, du filtrage DNS sur tout le réseau à l’IA locale, avec le matériel, les coûts, les compétences et les compromis de chaque niveau."
genre: ["Homelab", "Auto-hébergement", "IA locale", "Réseaux domestiques"]
tags: ["homelab", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "IA locale", "consommation électrique"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Un homelab évolue d’un petit Raspberry Pi et d’un routeur vers du stockage, des serveurs, du matériel réseau et un poste de travail d’IA locale."
coverCaption: ""
---

Construire un homelab en 10 niveaux, de Pi-hole à l’IA locale
============================================================

Un **homelab** est un ensemble d’ordinateurs et de services que vous gérez pour résoudre des problèmes quotidiens et apprendre à exploiter des systèmes réels. Vous pouvez bloquer les publicités, automatiser l’éclairage, stocker les médias de la famille ou tester des machines virtuelles. **Commencez par une tâche utile.** Ajoutez du matériel lorsqu’une limite réelle apparaît.

Ce guide part d’un petit Raspberry Pi exécutant Pi-hole et va jusqu’à un serveur de modèles d’IA locaux. **Chaque niveau ajoute une capacité et une nouvelle responsabilité.** Les estimations de coût utilisent une consommation indicative et un tarif électrique de $0.15 par kilowattheure. Vérifiez votre tarif local et mesurez votre matériel avant d’en acheter davantage.

## Niveau 1 : Bloquer les publicités sur tout le réseau domestique

Installez [Pi-hole](https://docs.pi-hole.net/) sur un Raspberry Pi ou un autre petit ordinateur Linux. Pi-hole agit comme un **puits DNS**. Lorsqu’un appareil demande l’adresse d’un domaine présent dans une liste de blocage, Pi-hole ne renvoie aucune destination exploitable. Le navigateur, le téléphone et la télévision connectée utilisent le même filtre si le routeur ou le serveur DHCP dirige les clients vers Pi-hole.

Le **filtrage DNS** agit aussi en dehors des navigateurs, notamment sur certaines publicités dans les applications et les téléviseurs connectés. Le contenu intégré aux pages échappe au filtre. Les publicités servies depuis le même domaine qu’un site ou une application passent donc. Une liste de blocage peut empêcher le chargement d’une connexion, d’une vidéo ou d’un paiement. Consultez le journal des requêtes Pi-hole, autorisez le domaine concerné si nécessaire et prévoyez un DNS de secours en cas de panne.

La consommation reste modeste. Pour un appareil de 8 watts qui fonctionne tout le mois, l’estimation est de 8 W × 24 heures × 30 jours ÷ 1 000 × $0.15 = **environ $0.86 par mois**. Mesurez l’alimentation complète à la prise. Un deuxième ordinateur, un disque USB ou un adaptateur inefficace change le total.

**Vous apprendrez :** DNS, DHCP, listes de blocage et maintenance Linux de base.

## Niveau 2 : Automatiser localement les appareils connectés

Ajoutez [Home Assistant](https://www.home-assistant.io/), qui rassemble les appareils connectés compatibles et les automatisations dans un seul système. Programmez l’extinction des lumières au coucher. Allumez un ventilateur lorsqu’un capteur de température dépasse un seuil défini. Recevez une alerte quand un détecteur de fuite repère de l’eau. **Ces petites automatisations apportent un avantage immédiat.**

Le **contrôle local** maintient de nombreuses automatisations dans votre maison lorsqu’un service externe ou la connexion Internet tombe en panne. Le comportement dépend de l’appareil. Certains produits exigent toujours un compte fournisseur, un service cloud ou une connexion Internet pour leur configuration et leurs fonctions à distance. Vérifiez les exigences de l’intégration avant d’acheter le matériel.

**Sauvegardez Home Assistant** et gardez une copie hors de son hôte. Documentez les intégrations et les étapes de récupération. Une carte SD ou un mini-PC défectueux ne doit pas effacer votre configuration.

**Vous apprendrez :** intégrations d’appareils, déclencheurs, conditions et récupération depuis une sauvegarde.

## Niveau 3 : Exécuter plusieurs services sur un mini-PC

Un **mini-PC professionnel d’occasion** offre souvent de la mémoire extensible, du stockage remplaçable et des ports utiles à bas prix. Un mini-PC Intel N100 consomme souvent moins et occupe peu de place. Intel décrit le N100 comme un processeur à quatre cœurs et quatre threads, avec un TDP de 6 watts et la prise en charge de jusqu’à 16 Go de mémoire. La valeur du processeur ne correspond pas à la consommation de tout le système à la prise. Comparez l’ordinateur précis, la mémoire, le stockage, la garantie et les ports réseau.

Installez Linux et utilisez [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) pour exécuter des services distincts dans des **conteneurs**. Un conteneur regroupe une application et ses dépendances tout en partageant le noyau du système d’exploitation hôte. Vous pouvez, par exemple, exécuter un gestionnaire de mots de passe comme le projet Vaultwarden maintenu par la communauté, ainsi qu’un moniteur de disponibilité comme Uptime Kuma. **Traitez le gestionnaire de mots de passe comme un service sensible :** limitez l’accès, utilisez une authentification forte, appliquez les mises à jour et gardez une sauvegarde chiffrée.

**Les conteneurs ne remplacent ni les mises à jour ni les sauvegardes.** Définissez un emplacement de stockage pour chaque service et consignez les étapes de récupération. Un mini-PC compact a aussi ses limites. Plusieurs bases de données, conversions multimédias ou grosses applications épuisent la mémoire, le stockage ou le temps processeur.

**Vous apprendrez :** administration Linux, conteneurs, volumes, mises à jour et récupération de services.

## Niveau 4 : Créer une médiathèque domestique

[Jellyfin](https://jellyfin.org/docs/) est un serveur multimédia open source. [Plex](https://support.plex.tv/) propose un écosystème de clients soigné et des fonctions facultatives liées à un compte. Les deux organisent des bibliothèques personnelles et diffusent les médias vers des clients compatibles. **Choisissez selon vos clients**, votre mode d’accès à distance, la prise en charge du matériel et les fonctions nécessaires.

**Vos besoins de stockage** dépendent de la taille et de la qualité de votre collection. Commencez avec un seul disque uniquement si vous avez déjà prévu une sauvegarde séparée. Utilisez des noms de dossiers et des métadonnées cohérents pour que le serveur associe correctement les films et les épisodes.

La **lecture directe** envoie un fichier compatible au client sans modifier son flux vidéo. Le **transcodage** convertit l’audio ou la vidéo lorsque le client, la connexion, les sous-titres ou le réglage de qualité réclame un autre format. Le transcodage sollicite davantage le serveur. Testez vos appareils et votre réseau avant d’acheter un GPU ou un processeur plus puissant. **Évitez un serveur multimédia dédié** si tous les clients lisent directement vos fichiers et qu’un seul hôte suffit.

**Vous apprendrez :** formats multimédias, planification du stockage, débit réseau et tests de charge.

## Niveau 5 : Ajouter de la redondance au stockage et une sauvegarde distincte

Un NAS à deux disques avec **stockage en miroir** écrit les données sur les deux disques. Si l’un tombe en panne, l’autre conserve une copie récente pendant que vous remplacez le disque défectueux et reconstruisez le miroir. Le miroir protège la disponibilité lors d’une panne d’un seul disque. **Un miroir ne restaure pas** un fichier supprimé, n’annule pas le chiffrement par rançongiciel et ne protège pas contre le vol, l’incendie ou un incident électrique qui endommage les deux disques.

Gardez une **sauvegarde distincte** sur un autre appareil ou dans un autre lieu. Incluez les documents importants, les photos, les exportations de configuration et les données des services. Suivez un calendrier de sauvegarde et conservez des versions pour éviter qu’une modification accidentelle écrase toutes les bonnes copies.

**Testez une restauration.** Sélectionnez quelques fichiers, restaurez-les dans un autre dossier et ouvrez-les. Pour un service, restaurez ses données dans une instance de test ou documentez les étapes et vérifiez chaque fichier. Une sauvegarde que vous n’avez jamais restaurée reste une hypothèse, pas un plan de récupération.

**Vous apprendrez :** systèmes de fichiers, remplacement de disques, rotation des sauvegardes et tests de restauration.

## Niveau 6 : Apprendre la virtualisation avec un petit cluster Proxmox

[Proxmox VE](https://pve.proxmox.com/pve-docs/) exécute des machines virtuelles et des conteneurs sur du matériel serveur. Plusieurs mini-PC réunis en **cluster** partagent une vue de gestion et permettent d’apprendre les nœuds, le stockage et la migration. Un cluster est un groupe de serveurs configurés pour se coordonner. Leurs mémoires ne forment pas un grand pool commun. **La haute disponibilité exige** une planification supplémentaire et un stockage partagé ou répliqué adapté.

Un **instantané** enregistre l’état d’une machine virtuelle à un moment précis et permet de revenir à un état antérieur après une modification dans le labo. Les instantanés dépendent généralement du stockage d’origine. Ils ne constituent pas des sauvegardes indépendantes. **Copiez les données importantes vers une cible de sauvegarde distincte** et testez la restauration.

Chaque nœud augmente la consommation, le nombre de ports réseau, les câbles et les mises à jour. Trois petits ordinateurs signifient aussi trois systèmes à corriger et à dépanner. Un seul mini-PC avec quelques machines virtuelles enseigne une grande partie des mêmes bases à moindre coût. **Ajoutez des nœuds lorsque** les expériences exigent une isolation ou que vous voulez pratiquer l’administration d’un cluster.

**Vous apprendrez :** machines virtuelles, pools de stockage, instantanés, appartenance au cluster et maintenance des nœuds.

## Niveau 7 : Ajouter un accès distant privé et séparer le réseau

[Tailscale](https://tailscale.com/kb/) connecte vos appareils approuvés par un réseau privé et donne accès à certains services domestiques lorsque vous êtes absent. **Limitez l’accès** aux appareils et aux services nécessaires à chaque personne. Protégez les comptes avec l’authentification multifacteur et examinez les anciens appareils et clés.

Un commutateur géré ou un routeur avec prise en charge des **VLAN** sépare les groupes d’appareils. Placez les prises connectées et les appareils peu fiables sur un réseau différent de celui des ordinateurs qui contiennent des fichiers personnels. Placez le stockage sur un réseau accessible uniquement aux systèmes qui en ont besoin. La segmentation limite les communications entre appareils. Maintenez aussi les mises à jour, les mots de passe solides et les règles d’accès.

**N’exposez pas directement les interfaces d’administration sur Internet** sans comprendre les exigences d’authentification, de correctifs et de pare-feu du service. Un outil d’accès privé exige lui aussi un contrôle rigoureux des comptes et des appareils.

**Vous apprendrez :** accès privé, autorisations fondées sur l’identité, VLAN, règles de pare-feu et limites de confiance entre appareils.

## Niveau 8 : Ajouter un serveur d’entreprise

Passez à un serveur plus grand lorsque vos mesures montrent qu’il vous faut davantage de cœurs CPU, de mémoire, de baies de disques, de ports PCIe ou de capacité réseau. Les anciens serveurs d’entreprise coûtent souvent moins cher d’occasion, mais leurs ventilateurs sont bruyants et leur **consommation au repos atteint environ 100 à 160 watts**, selon le modèle et les composants installés. Considérez cette plage comme une estimation, pas comme une spécification.

Calculez une estimation annuelle de l’électricité avant l’achat :

`watts mesurés ÷ 1 000 × 24 × 365 × tarif électrique par kWh`

À 120 watts et $0.15 par kWh, l’estimation est de 1 051 kWh par an, soit environ **$158 par an**. Mesurez le serveur précis au repos et pendant votre charge habituelle. Ajoutez la consommation des disques, du refroidissement et de l’onduleur.

Vérifiez la profondeur du châssis, la compatibilité des disques, le bruit, la commande des ventilateurs, l’alimentation et les cartes d’extension. Un serveur qui dépasse votre budget d’espace ou d’électricité n’est pas une amélioration pratique.

**Vous apprendrez :** matériel serveur, gestion à distance, extensions, refroidissement et estimation des coûts d’exploitation.

## Niveau 9 : Mesurer l’énergie et dimensionner le labo

Utilisez un **wattmètre de prise** pour mesurer chaque ordinateur au repos et en fonctionnement normal. Dressez la liste des plus gros consommateurs. Examinez les réglages d’alimentation du BIOS, retirez les cartes et disques inutilisés et replacez les services du quotidien sur des mini-PC efficaces lorsque le matériel d’entreprise n’est pas nécessaire.

Ne démarrez le grand serveur que lorsqu’une charge en a besoin. Si vous utilisez un programme Wake-on-LAN ou une commande d’alimentation à distance, documentez les étapes de récupération en cas de panne réseau ou électrique. Tenez une **liste des dépendances entre services** pour éviter qu’un arrêt interrompe le stockage ou le réseau requis par d’autres systèmes.

Une baie organise le matériel et la circulation de l’air lorsque l’équipement rackable justifie l’espace. Un onduleur couvre les coupures brèves et laisse le temps aux systèmes de s’arrêter proprement. Les deux ajoutent des coûts d’achat, de l’espace et une consommation continue. **Mesurez leur consommation** et incluez le remplacement des batteries dans votre budget à long terme.

**Vous apprendrez :** mesure de l’énergie, gestion de l’alimentation, cartographie des dépendances et planification de capacité.

## Niveau 10 : Exécuter des modèles d’IA en local

[Ollama](https://docs.ollama.com/) télécharge des modèles de langage pris en charge et les exécute sur votre ordinateur. L’**inférence locale** conserve les requêtes et les réponses sur du matériel que vous contrôlez lorsque vous utilisez un modèle et une application locaux. Vérifiez que tout le parcours logiciel reste local. Une application connectée, une fonction de télémétrie ou une option de modèle cloud envoie des données hors de votre réseau.

Les besoins matériels dépendent de la taille du modèle, de la quantification, de la longueur du contexte et de la vitesse visée. **La mémoire système ou la mémoire GPU doit contenir** les poids du modèle et le contexte de travail. Les petits ordinateurs exécutent de petits modèles, tandis que les gros modèles et les longs contextes demandent davantage de mémoire et souvent un GPU performant. Mesurez la consommation pendant l’inférence. Un système équipé d’un GPU consomme souvent bien plus qu’un mini-PC au repos.

Les modèles locaux conviennent à la rédaction de brouillons, au résumé de notes privées et à la classification simple si leur qualité répond à vos besoins. Ils donnent des réponses incorrectes et les petits modèles peinent souvent avec le raisonnement complexe ou les faits récents. Les modèles cloud réussissent parfois mieux certaines tâches. **Comparez la qualité, la confidentialité, la latence, le coût et l’énergie** avant de choisir où exécuter une charge.

**Vous apprendrez :** mémoire des modèles, quantification, inférence, limites de confidentialité et évaluation des charges.

## Comparer les dix niveaux

**Les coûts sont des estimations, pas des devis.** Les prix du matériel varient selon la région, l’état et la configuration de stockage. Estimez l’électricité avec `watts ÷ 1 000 × heures × jours × tarif par kWh`. Mesurez à la prise si possible et incluez les heures au repos, car de nombreux serveurs domestiques fonctionnent en continu.

### Capacités et matériel

| Niveau | Nouvelle capacité | Matériel habituel |
|---|---|---|
| **1** | Filtrage DNS du réseau | Raspberry Pi ou petit hôte Linux |
| **2** | Automatisation locale des appareils | Pi ou mini-PC, appareils compatibles |
| **3** | Plusieurs applications auto-hébergées | Mini-PC professionnel d’occasion ou système N100 |
| **4** | Diffusion de médias personnels | Mini-PC et stockage multimédia |
| **5** | Tolérance à la panne d’un disque et récupération | NAS à deux disques et sauvegarde séparée |
| **6** | Labo de serveurs virtuels | Deux mini-PC ou plus |
| **7** | Accès privé et segmentation | Tailscale, routeur ou commutateur géré |
| **8** | Forte capacité et extensions | Serveur d’entreprise |
| **9** | Réduction de la consommation du labo | Wattmètre, systèmes réglés |
| **10** | Inférence locale de modèles | PC avec beaucoup de mémoire, GPU facultatif |

### Compétences, coûts et compromis

| Niveau | Compétences acquises | Estimation des coûts récurrents | Principal compromis |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Environ $1/mois à 8 W et $0.15/kWh | Certaines publicités restent et les faux positifs demandent une vérification |
| **2** | Intégrations, déclencheurs, sauvegardes | Alimentation de l’hôte et coûts des appareils | Compatibilité et travail de sauvegarde |
| **3** | Docker, mises à jour, stockage | Dépend de la consommation mesurée | Limites CPU, mémoire et disque |
| **4** | Formats, organisation, transcodage | Stockage et énergie du serveur | Le transcodage demande parfois plus de matériel |
| **5** | Miroir, conservation, restauration | Énergie du NAS, disques, cible de sauvegarde | Un miroir n’est pas une sauvegarde |
| **6** | Proxmox, VM, clusters | Chaque nœud ajoute consommation et entretien | Plus de nœuds signifie plus de maintenance |
| **7** | Règles d’accès, VLAN, pare-feu | Équipement réseau et coûts de service | Des règles incorrectes exposent les services |
| **8** | Matériel, refroidissement, gestion à distance | Variable selon le serveur, calculez avec les mesures | Bruit, chaleur et consommation au repos |
| **9** | Mesure, planification, dimensionnement | Achat ponctuel du wattmètre, économies variables | La planification ajoute des tâches opérationnelles |
| **10** | Déploiement et évaluation de modèles | Énergie de calcul et stockage | Qualité et vitesse dépendent du matériel |

## Choisir la prochaine amélioration utile

**Arrêtez-vous au niveau qui répond à vos besoins actuels.** Pi-hole et un mini-PC peuvent suffire à vos services. Un NAS est utile si vous avez besoin d’un stockage partagé et d’un plan de récupération testé. Ajoutez un cluster ou un serveur d’entreprise lorsqu’une charge ou un objectif d’apprentissage le justifie.

Notez **où se trouvent les données de chaque service, comment le mettre à jour et comment le restaurer.** Testez les sauvegardes avant d’ajouter du matériel. Laissez la prochaine limite réelle guider votre prochain achat.

## Références

- [Documentation Pi-hole](https://docs.pi-hole.net/)
- [Documentation Home Assistant](https://www.home-assistant.io/docs/)
- [Caractéristiques du processeur Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker : Qu’est-ce qu’un conteneur ?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentation Jellyfin](https://jellyfin.org/docs/)
- [Assistance Plex](https://support.plex.tv/)
- [Documentation Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentation Tailscale](https://tailscale.com/kb/)
- [Documentation Ollama](https://docs.ollama.com/)
