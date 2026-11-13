---
title: "Open WebUI v0.12.4 : checklist de mise à niveau et de contrôle d’accès 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Sauvegardez et mettez à niveau Open WebUI vers v0.12.4, puis testez le partage des chats, les autorisations d’exportation, les accès aux ressources, les comptes et l’accès réseau."
genre: ["IA auto-hébergée", "Cybersécurité", "Administration système"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "mise à niveau Open WebUI", "sécurité Open WebUI", "contrôle d’accès Open WebUI", "IA auto-hébergée", "mise à niveau Docker", "mise à niveau pip", "sauvegarde Open WebUI", "autorisations Open WebUI", "rôles Open WebUI", "groupes Open WebUI", "autorisation d’exportation des chats", "chats partagés", "chats archivés", "accès à la base de connaissances", "accès aux modèles", "autorisations des outils", "sécurité des clés API", "sécurité du compte administrateur", "désactiver les inscriptions", "authentification du proxy inverse", "accès VPN", "épinglage de l’image de conteneur"]
---

**Open WebUI v0.12.4 contient des correctifs de sécurité que les responsables du projet n’ont pas encore détaillés.** Les notes de version recommandent de mettre les déploiements à jour rapidement et indiquent que des avis suivront l’attribution des CVE. Les changements nommés ci-dessous concernant le partage des chats et les autorisations sont les éléments visibles dans les notes de version, et non une liste complète des correctifs de sécurité non divulgués. [Notes de version Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Points clés

- **Sauvegardez d’abord.** Conservez une copie récupérable du volume de données ou de la base de données et des téléversements avant de modifier l’application.
- **Épinglez la version officielle.** Utilisez `ghcr.io/open-webui/open-webui:v0.12.4` pour l’image Docker standard ou `open-webui==0.12.4` pour pip.
- **Testez les autorisations avec de vrais rôles utilisateur.** Un bouton masqué ne prouve pas qu’une vérification d’autorisation côté API existe.
- **Gardez l’accès privé.** Exigez l’authentification de l’application et limitez l’accès réseau au moyen d’un VPN ou d’un proxy inverse authentifié.

## Avant la mise à niveau

**Prérequis :** identifiez la méthode d’installation actuelle, la variante de l’image de conteneur, l’emplacement des données persistantes, la base de données externe, le proxy inverse et le fournisseur d’authentification. Planifiez une fenêtre d’interruption et conservez la configuration du conteneur ou la définition du service existante. Prévoyez du temps pour répéter une restauration sur une instance séparée. Les commandes ci-dessous sont des modèles documentés par le fournisseur et adaptés à cette version épinglée. Elles ne correspondent pas à une mise à niveau réelle effectuée pour ce guide. [Mettre à jour Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Inventoriez le stockage.** Dans la configuration Docker standard, `open-webui` monte `/app/backend/data`. Notez les montages liés, la base de données externe, le stockage objet et les variables d’environnement personnalisées. Avec pip, repérez le répertoire de données actif de l’application et la base de données avant de modifier l’environnement. Ne supposez pas qu’un export de chat constitue une sauvegarde complète.
2. **Sauvegardez après avoir arrêté les écritures.** Arrêtez l’application ou utilisez un instantané cohérent de la base de données, puis copiez le volume, toute base de données externe et les téléversements vers un stockage distinct. Le fournisseur documente une archive de volume Docker. Adaptez le nom du volume et le chemin de sauvegarde à votre déploiement. Vérifiez que l’archive s’ouvre et répétez une restauration sur une instance séparée avant de vous y fier. [Sauvegarde et restauration](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Lisez les notes de version et les consignes de migration.** Les notes v0.12.4 ne détaillent pas les correctifs de sécurité en attente et ne donnent pas leur plage de versions concernées. N’attribuez pas de CVE à ces correctifs et ne supposez pas que toute version antérieure à v0.12.4 est touchée par une faille précise. Le guide de mise à jour avertit que certaines migrations de base de données sont à sens unique et que des réplicas de versions différentes posent problème. Si plusieurs processus ou réplicas partagent une base de données, arrêtez-les ensemble et suivez la [procédure de migration multi-réplica](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Une restauration peut nécessiter la sauvegarde de la base de données antérieure à la mise à niveau.

## Mettre à niveau le paquet installé

**Docker, procédure du fournisseur adaptée à une balise épinglée :** après la sauvegarde, récupérez l’image standard officielle et recréez le conteneur avec le *même* volume persistant, la même configuration et le même `WEBUI_SECRET_KEY`. Cet exemple suppose le volume nommé par défaut et un proxy lié localement en amont. Ne collez pas votre vraie clé dans l’historique du shell. Fournissez-la par votre mécanisme existant d’environnement protégé ou de gestion des secrets. Conservez les options GPU, Ollama, réseau personnalisé, base de données et autres de votre déploiement actuel. [Mettre à jour Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Balises officielles des images](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Vérifiez `./open-webui.env` avant l’exécution :** le fichier doit déjà exister, avoir des permissions restrictives et contenir votre `WEBUI_SECRET_KEY` actuel ainsi que la configuration requise. La liaison à l’interface locale convient à un proxy sur le même hôte, pas à un proxy sur une autre machine. Avec Compose, modifiez uniquement l’image du service pour utiliser la balise épinglée, puis exécutez `docker compose pull open-webui` et `docker compose up -d open-webui` dans le projet existant. Gardez le même volume et la même configuration d’environnement. Ces commandes sont des suggestions, pas la migration testée de votre déploiement.

**pip, procédure de mise à jour du fournisseur avec une version fixe :** dans l’environnement virtuel existant, arrêtez le service, installez exactement cette version du paquet et redémarrez-le avec le même répertoire de données et le même environnement. Évitez un second environnement Python ou une nouvelle base de données vide. La consigne générique du fournisseur utilise `pip install -U open-webui`. La contrainte de version ci-dessous épingle cette checklist à v0.12.4. [Mettre à jour Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Démarrage rapide](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Vérifiez le service en cours d’exécution, pas seulement l’artefact installé.** Consultez la version au démarrage dans `docker logs open-webui` ou dans les journaux du service pip et comparez-la à la version affichée dans l’application après connexion. Le guide de mise à jour du fournisseur recommande de vérifier les journaux du conteneur et de charger la page de connexion. Si l’interface affiche des ressources obsolètes, forcez l’actualisation du navigateur. Si le démarrage signale une erreur de migration, laissez le service indisponible jusqu’à ce que vous ayez diagnostiqué le problème. Ne remettez pas un ancien binaire sur une base de données migrée sans vérifier les exigences de restauration. [Vérifications après mise à jour](https://docs.openwebui.com/getting-started/updating/)

## Vérifier les accès après le redémarrage

**Comportement indiqué par le fournisseur :** dans v0.12.4, les actions d’exportation des dossiers et des chats archivés, ainsi que la copie des chats, sont masquées pour les utilisateurs sans l’autorisation **Allow Chat Export**. Les contrôles d’accès aux modèles, prompts, outils, connaissances, compétences, notes et dossiers sont aussi masqués pour les utilisateurs sans l’autorisation de partage correspondante. Les personnes qui consultent un dossier partagé ne reçoivent plus les mises à jour en direct d’un chat après son archivage par le propriétaire. Les personnes qui consultent un lien de partage ne reçoivent plus de mises à jour en direct après que le propriétaire a annulé le partage de tous les chats. Des contrôles masqués sont un comportement de l’interface, pas la preuve qu’un correctif côté serveur a été apporté à une vulnérabilité non précisée. [Notes de version](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Vérification recommandée pour l’opérateur :** avec un compte de test sans autorisations d’exportation et de partage, vérifiez l’absence des actions nommées. Avec un compte autorisé, confirmez que les actions prévues fonctionnent toujours. Créez un chat de test non sensible dans un dossier partagé, consultez-le depuis un autre compte, archivez-le comme propriétaire et confirmez que les nouvelles mises à jour ne sont plus envoyées à l’autre personne. Répétez avec un lien de partage et **Unshare All Chats**. Revérifiez les droits enregistrés et les anciens liens au lieu de supposer que le contenu archivé ou les copies historiques ont été effacés.

| Domaine de contrôle | Éléments à vérifier |
|---|---|
| **Rôles et groupes** | Supprimez les membres et affectations d’administrateur obsolètes. Vérifiez les autorisations effectives d’un utilisateur nouvellement approuvé et d’un utilisateur restreint. |
| **Modèles et outils** | Examinez les droits d’accès de chaque modèle, les outils associés, les droits de création d’outils et les identifiants du fournisseur. Testez avec un compte sans droits d’administration. |
| **Connaissances et fichiers** | Inspectez les collaborateurs de la base de connaissances, les droits sur les ressources, les pièces jointes et les paramètres de partage. Vérifiez un compte dont l’accès a été supprimé. |
| **Chats et exportations** | Examinez les dossiers partagés, les liens de partage, les chats archivés et les affectations Allow Chat Export. Révoquez les liens inutiles. |

Ces contrôles d’inventaire sont des **recommandations d’opérateur**, pas de nouvelles garanties introduites par v0.12.4. Le [guide de renforcement](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) du fournisseur documente les rôles à plusieurs niveaux, les groupes, les droits par ressource, les autorisations de l’espace de travail, les clés API et le placement réseau.

## Combler les lacunes liées aux comptes et au réseau

- **Inscriptions, paramètre du fournisseur :** désactivez les inscriptions ouvertes si un administrateur ou un fournisseur d’identité crée les comptes. Vérifiez `ENABLE_SIGNUP` et les paramètres administrateur persistants avec le [guide de renforcement](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Maintenez des règles d’approbation strictes pour les nouveaux comptes.
- **Clés API, examen par l’opérateur :** inventoriez les clés émises, supprimez celles qui ne servent plus et limitez leur création et l’accès aux points de terminaison aux rôles et routes nécessaires. Selon le guide de renforcement du fournisseur, une clé agit avec les autorisations de son créateur. Gardez les clés hors des exemples de l’article et des journaux de l’application.
- **Administrateurs, examen par l’opérateur :** supprimez les comptes administrateur abandonnés, imposez des contrôles de connexion robustes, vérifiez la disponibilité de l’authentification multifacteur et recherchez les changements de compte inattendus. Testez la procédure de récupération du compte avant de désactiver un administrateur redondant.
- **Limite réseau, recommandations du fournisseur :** placez le service derrière un VPN, un proxy d’accès ou un proxy inverse avec authentification et liste d’adresses IP autorisées. Ne l’exposez pas publiquement sans authentification. Évitez `WEBUI_AUTH=False` sur un service accessible. Un proxy inverse sans authentification propre ne remplace pas à lui seul la connexion à l’application. [Renforcer Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Portée :** cette checklist couvre la version officielle d’Open WebUI et ses méthodes d’installation standard documentées. Elle ne vérifie pas les forks, les images dérivées ni les paquets tiers. Les notes v0.12.4 ne signalent pas d’exploitation active. Consultez les [avis de sécurité du projet](https://github.com/open-webui/open-webui/security/advisories) pour les divulgations ultérieures et leurs propres versions concernées et corrigées. N’attribuez pas à v0.12.4 le correctif d’un avis antérieur sans lire sa plage de versions.

## Sources et références

- [Notes de version Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avis de sécurité Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Mettre à jour Open WebUI, y compris sauvegarde, restauration et migrations](https://docs.openwebui.com/getting-started/updating/)
- [Démarrage rapide Open WebUI et balises officielles](https://docs.openwebui.com/getting-started/quick-start/)
- [Renforcer Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Mises à jour et migrations multi-réplica](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
