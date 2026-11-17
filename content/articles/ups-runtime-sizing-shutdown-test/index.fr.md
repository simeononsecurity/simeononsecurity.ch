---
title: "Dimensionner un onduleur pour un homelab et tester l’arrêt automatique"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Mesurez la consommation de votre homelab, comparez les limites en watts et en VA de l’onduleur, vérifiez l’autonomie selon votre charge et testez un arrêt propre avant de vous fier à la batterie."
genre: ["Laboratoire domestique", "Protection électrique", "Administration système"]
tags: ["onduleur homelab", "dimensionnement onduleur", "autonomie onduleur", "arrêt automatique", "Network UPS Tools", "watts onduleur", "VA onduleur", "facteur de puissance", "alimentation de secours", "arrêt serveur", "arrêt NAS", "coupure de courant", "test onduleur", "courbe d’autonomie", "wattmètre", "surveillance onduleur", "remplacement de batterie", "protection contre les surtensions", "arrêt ordonné", "alimentation homelab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Un onduleur de homelab alimente un serveur, un NAS, un routeur et un commutateur au-dessus d’une chronologie allant de la coupure à l’arrêt."
coverCaption: "Mesurez la charge, vérifiez l’autonomie et testez l’arrêt avant une coupure de courant."
---

Un **onduleur**, ou alimentation sans coupure, donne à votre homelab le temps d’enregistrer le travail et d’arrêter les systèmes pendant une coupure de courant. Son étiquette ne vous indique pas combien de temps vos serveurs fonctionneront. Vous devez connaître la charge des équipements, les limites en watts et en VA de l’onduleur, une estimation d’autonomie pour cette charge et une procédure d’arrêt testée.

## À retenir

- **Mesurez la charge :** Notez la consommation normale et maximale de chaque appareil que vous voulez maintenir sur batterie.
- **Vérifiez les deux valeurs :** L’onduleur doit respecter les besoins en watts et en VA des équipements connectés.
- **Consultez la courbe d’autonomie :** L’autonomie dépend de la charge et de l’état de la batterie. Utilisez une estimation propre au modèle.
- **Testez l’arrêt :** Vérifiez que le signal de l’onduleur atteint chaque hôte et que les hôtes s’arrêtent avant l’épuisement de la batterie.

## Avant de commencer

Vous avez besoin d’un wattmètre adapté à votre alimentation secteur, d’une liste des appareils et de leurs adaptateurs, ainsi que des caractéristiques et de la courbe d’autonomie de chaque modèle d’onduleur envisagé. Pour un test d’arrêt automatique, vous avez aussi besoin d’une connexion USB ou de gestion réseau prise en charge et d’un logiciel pour chaque hôte. Prévoyez le temps nécessaire à une mesure en charge normale, une observation en charge élevée et un test de maintenance planifié. Cette tâche est de niveau intermédiaire pour un homelab, car un test d’arrêt complet interrompt les services.

Le [guide des parasurtenseurs](/articles/protecting-your-tech_-the-best-surge-protectors/) du site traite de la protection contre les surtensions. Le [comparatif de modèles d’onduleurs](/articles/best-ups-models-for-uninterrupted-connectivity/) présente des produits. Ce guide porte sur le dimensionnement et la vérification de votre propre charge. Le [guide de dimensionnement d’Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) et le [guide d’achat de Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) distinguent tous deux la puissance de sortie de l’autonomie de la batterie.

> **Avertissement :** Utilisez uniquement les prises et charges approuvées par le fabricant de l’onduleur. Respectez sa capacité nominale pendant le test. Un véritable test d’arrêt interrompt le laboratoire connecté.

## Mesurez les équipements à maintenir sous tension

Décidez quels appareils doivent fonctionner jusqu’à l’arrêt. Incluez l’hyperviseur, le stockage, le commutateur réseau et le routeur si un hôte a besoin d’un accès réseau pour recevoir un signal d’arrêt. Laissez les écrans, imprimantes et autres charges facultatives hors des prises secourues par batterie, sauf si votre plan les exige.

Mesurez à la prise le groupe prévu pour l’alimentation sur batterie. Notez les **watts en fonctionnement normal** et la puissance maximale observée lors d’une activité représentative, par exemple le démarrage des hôtes ou des machines virtuelles. L’étiquette d’une alimentation indique sa capacité, pas la consommation mesurée du système. Vérifiez tout de même les limites d’entrée et de courant d’appel indiquées sur les appareils. Consignez les conditions de mesure dans votre feuille de calcul.

| Appareil | Watts en fonctionnement normal | Pic observé en watts | Prise sur batterie ? |
|---|---:|---:|---|
| **Routeur et commutateur** | 30 | 35 | Oui |
| **NAS** | 60 | 90 | Oui |
| **Petit serveur** | 90 | 135 | Oui |
| **Total indicatif** | **180** | **260** | Trois appareils |

Les valeurs ci-dessus sont **indicatives**, et non des mesures d’un laboratoire précis. Votre charge varie avec les disques, les GPU, les réglages d’alimentation et les équipements connectés. Recommencez les mesures après toute modification matérielle importante.

## Distinguez puissance active et puissance apparente

Les **watts** décrivent la puissance réelle utilisée par les équipements. Les **voltampères (VA)** décrivent la puissance apparente. Le rapport dépend du **facteur de puissance** : les watts divisés par le facteur de puissance donnent les VA. Eaton explique ce calcul dans son [guide de dimensionnement](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Ne considérez pas une indication de 1000 VA comme équivalente à 1000 watts. Vérifiez la puissance en watts distincte de l’onduleur.

Pour le pic indicatif de 260 W, une marge de capacité de 25 % donne **325 W**. Schneider Electric recommande une puissance de sortie environ [20 % à 25 % supérieure à la charge](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Choisissez un onduleur dont la puissance continue en watts dépasse le pic prévu, marge comprise. Si vous connaissez le facteur de puissance combiné, divisez les watts de pointe par ce facteur pour estimer les VA de pointe, puis appliquez la marge choisie aux VA. Sinon, utilisez un appareil de mesure adapté ou le sélecteur du fabricant pour déterminer les besoins en VA et la marge. N’inventez pas de facteur de puissance si vous ne l’avez pas mesuré.

Une marge de capacité ne garantit pas l’autonomie. Un onduleur avec une limite élevée en watts mais une petite batterie peut alimenter la charge pendant peu de temps. Avant de choisir un modèle, vérifiez les prises, le type de fiche, la tension d’entrée, l’interface de communication et les possibilités de remplacement de la batterie.

## Fixez un objectif d’autonomie

Notez le temps nécessaire au laboratoire pour s’arrêter en toute sécurité. Tenez compte du délai d’envoi de l’alerte d’arrêt aux hôtes, de l’arrêt des machines virtuelles, de la vidange des écritures du stockage et de la coupure de la sortie de l’onduleur. Ajoutez une réserve pour un arrêt lent et une batterie vieillissante. Un laboratoire qui doit tenir pendant de brèves coupures a un objectif différent d’un laboratoire qui doit uniquement s’arrêter proprement.

À titre d’**exemple**, supposons qu’un arrêt testé prenne 6 minutes et que vous ajoutiez 5 minutes de réserve. Il faut donc au moins 11 minutes d’autonomie à la charge prévue. C’est un exemple de planification, pas un seuil universel. Comparez cet objectif à la courbe ou au sélecteur du modèle envisagé pour votre **charge normale et maximale mesurée**, puis réévaluez-le à mesure que la batterie vieillit. Le [sélecteur d’onduleurs de Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) estime l’autonomie à partir de la charge saisie et des caractéristiques du modèle. Eaton renvoie également aux données propres à chaque modèle dans son [guide des onduleurs de bureau](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copiez cette **feuille de calcul** pour votre laboratoire. Remplissez les lignes des appareils à partir des mesures du wattmètre. Additionnez les watts en fonctionnement normal et en charge élevée, ajoutez la marge choisie au total élevé, puis appliquez la même marge aux VA de pointe mesurés ou calculés. Comparez ces deux résultats avec un onduleur candidat. Si vous utilisez un sélecteur du fabricant, notez son résultat VA et la marge. Estimez l’autonomie à partir de la courbe du modèle. Complétez les lignes relatives aux durées et à la récupération pendant le test.

| Champ | Votre résultat |
|---|---|
| **Appareils et prises secourues** | Noms des appareils et prise attribuée à chacun |
| **Watts normaux par appareil et total** | Valeurs mesurées et somme |
| **Watts élevés par appareil et total** | Valeurs maximales observées et somme |
| **Facteur de puissance mesuré ou spécifié** | Valeur et source, ou « inconnu » |
| **VA de pointe mesurés ou calculés** | Watts de pointe divisés par le facteur de puissance combiné, s’il est connu |
| **Marge de capacité** | Pourcentage choisi, puis watts et VA après marge |
| **Caractéristiques de l’onduleur candidat** | Modèle, watts et VA en sortie, limites des prises |
| **Objectif et estimation d’autonomie** | Minutes requises et estimation du modèle pour votre charge |
| **Heures d’alerte et d’arrêt** | Heure de l’alerte batterie et arrêt du dernier hôte |
| **Résultat de récupération** | Démarrage des hôtes, stockage, applications et supervision |

Si le facteur de puissance est inconnu, utilisez l’outil de sélection du fabricant ou mesurez la puissance apparente avec un appareil adapté. Ne communiquez pas de valeur VA calculée à partir d’un facteur supposé. La feuille n’est complète que lorsque le modèle respecte les deux limites de sortie et que son autonomie estimée dépasse votre objectif d’arrêt.

> **Résultat attendu :** Votre feuille nomme les appareils connectés, les charges mesurées, les limites en watts et VA de l’onduleur, l’objectif d’autonomie et l’estimation propre au modèle.

## Planifiez l’arrêt automatique

Un onduleur alimente temporairement les équipements. L’hôte a toujours besoin d’un **signal d’arrêt**. Vérifiez si l’onduleur fournit un port USB, une carte de gestion réseau ou une autre interface prise en charge. Vérifiez que chaque hôte à arrêter possède un chemin de supervision compatible. Eaton précise que de nombreux modèles prennent en charge la communication USB ou réseau nécessaire à un [arrêt propre d’un NAS ou d’un serveur](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Dans un laboratoire Linux utilisant **Network UPS Tools (NUT)**, le pilote lit l’onduleur, `upsd` partage son état et `upsmon` déclenche l’arrêt de l’hôte lorsque l’alimentation devient critique. Un hôte relié directement à un onduleur USB ou série exécute normalement le pilote, `upsd` et `upsmon` en mode **Primary**. Les autres hôtes exécutent `upsmon` en mode **Secondary** auprès de ce serveur. Un onduleur administré sur le réseau nécessite un pilote compatible et une configuration primaire propre au modèle. Le [guide de topologie NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) décrit ces rôles. Configurez le routeur et le commutateur pour que les hôtes de supervision restent connectés sur batterie. Réservez la commande d’arrêt et les autorisations associées aux administrateurs.

Avant un test d’arrêt, vérifiez que le pilote fournit un état à jour. Remplacez `myupsname` par le nom de l’onduleur dans votre configuration NUT :

```bash
upsc myupsname@localhost ups.status
```

Le [guide de configuration NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) attend `OL` pour une alimentation secteur normale et explique `OB` pour le fonctionnement sur batterie. Exécutez cette vérification sur chaque hôte qui supervise l’onduleur et utilisez le bon nom de serveur pour les clients distants. Une valeur absente ou obsolète indique que le chemin du signal doit être réparé avant le test.

Notez l’**ordre d’arrêt**. Par exemple, arrêtez d’abord les VM applicatives, puis les clients de stockage, et enfin l’hyperviseur et le NAS. Vérifiez que chaque service et système de fichiers se rétablit normalement après le retour du courant. L’arrêt réussi d’un hôte sans récupération saine des applications ne constitue pas un test complet.

## Testez sans supposer

Commencez par une **simulation** sur l’hôte où le pilote de l’onduleur est configuré. NUT décrit `upsdrvctl -t shutdown` comme un aperçu de la séquence d’arrêt du pilote. La commande n’appelle pas les pilotes et ne coupe pas l’alimentation :

```bash
upsdrvctl -t shutdown
```

Cette **simulation du pilote** ne prouve pas qu’une alerte de coupure atteint chaque hôte. Vérifiez chaque service de supervision et ses journaux. Pendant une fenêtre de maintenance, le [guide NUT des tests d’arrêt](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) décrit un test forcé avec `upsmon -c fsd` sur l’hôte NUT primaire. Ce **test FSD** lance une vraie séquence d’arrêt. Le marqueur FSD reste actif jusqu’au redémarrage de `upsd`. Au retour des systèmes, confirmez que `upsd` a redémarré et que l’état n’indique plus FSD avant de vous fier de nouveau à la supervision. Lisez le [manuel actuel d’upsmon](https://networkupstools.org/docs/man/upsmon.html), préparez une méthode de récupération et ne lancez le test qu’après avoir enregistré le travail et averti les utilisateurs du laboratoire.

Pour un **test contrôlé de passage sur batterie**, suivez d’abord la procédure du fabricant avec des charges non critiques. Cette vérification à faible charge contrôle la transmission du signal, mais ne prouve pas l’autonomie de votre laboratoire. Plus tard, pendant une fenêtre de maintenance, testez une charge sur batterie représentative de votre usage prévu. Une personne doit surveiller l’onduleur et pouvoir rétablir l’alimentation secteur si la réserve diminue. Notez la charge affichée par l’onduleur, l’heure du passage sur batterie, le début de l’arrêt de chaque hôte et l’heure d’arrêt du dernier. Vérifiez que la batterie ne s’épuise pas avant l’arrêt des hôtes. Après le retour du secteur, contrôlez le démarrage des hôtes, l’état des applications, l’intégrité du stockage et la supervision. Selon NUT, une séquence réussit si le système d’exploitation s’arrête avant la fin de la batterie et reprend son fonctionnement quand le courant revient.

| Vérification | À consigner |
|---|---|
| **Chemin du signal** | Événement de l’onduleur visible par chaque hôte de supervision |
| **Durée de l’arrêt** | Dernier hôte arrêté avant l’épuisement de la batterie |
| **Récupération** | Démarrage correct des hôtes, du stockage et des applications |
| **Capacité** | Charge de l’onduleur dans les limites en watts et VA |

## Dépannage

- **Alarme de surcharge de l’onduleur :** Retirez les charges facultatives. Comparez la charge élevée mesurée aux deux caractéristiques de l’onduleur et aux limites de ses prises.
- **Autonomie plus courte que prévu :** Vérifiez la charge actuelle, l’âge de la batterie, les données d’autonomie propres au modèle et les derniers tests de batterie. N’extrapolez pas linéairement à partir des seuls VA.
- **Un hôte reste allumé :** Vérifiez son service de supervision, le réseau, les autorisations d’arrêt et les journaux.
- **Les hôtes s’arrêtent mais ne redémarrent pas :** Vérifiez le comportement des sorties de l’onduleur au retour du courant, le réglage firmware de remise sous tension et les [considérations NUT sur les courses liées à l’alimentation](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **La simulation réussit, mais pas le test de coupure :** L’aperçu du pilote couvre un chemin plus limité. Vérifiez la transmission des événements et l’ordre d’arrêt réel des hôtes.

## Étapes suivantes

Conservez la feuille avec l’inventaire de votre homelab. Reprenez les mesures après l’ajout de matériel et répétez le test d’arrêt après une modification de l’onduleur, du logiciel de supervision, de la politique de démarrage des hôtes ou de la pile de stockage. Vérifiez séparément votre plan de sauvegarde et de restauration. La batterie protège la période d’arrêt, tandis qu’une [sauvegarde de homelab testée](/articles/what-is-a-homelab-and-should-you-have-one/) protège vos données contre d’autres pannes.
