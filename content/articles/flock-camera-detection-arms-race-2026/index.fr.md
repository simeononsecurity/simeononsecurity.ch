---
title: "Course à la détection des caméras Flock : les changements de 2026"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Passe en revue les changements signalés dans la détection de Flock Safety, les réponses de la communauté et les méthodes infrarouges pour repérer les caméras."
genre: ["Technologies de confidentialité", "Contre-surveillance", "Projets open source", "Droits numériques", "Sécurité réseau", "Recherche en sécurité", "Modification de matériel", "Outils de confidentialité"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Détection OUI", "Requête probe wildcard", "Mode WiFi promiscuité", "Surveillance 802.11", "DeFlockJoplin", "NitekryDPaul", "Détection BLE", "WiFi 5 GHz", "MAC administrée localement", "Correspondance de motifs SSID", "Matériel de contre-surveillance", "STS Collective", "colonelpanichacks", "Évasion de détection", "ESP32", "Détection WiFi", "Sensibilisation à la surveillance", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Suivi des tickets GitHub", "Mise à jour du firmware", "Protection contre l’empreinte numérique des appareils", "Randomisation MAC", "Fingerprinting des éléments d'information", "Saut de canal", "Défense de la confidentialité", "Sécurité open source", "Surveillance de masse", "Firmware de détection", "Détection WiFi en déplacement", "Retrait de caméras", "Matériel de confidentialité", "Détection infrarouge", "Éclairage IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Détection optique", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Scène urbaine avec une caméra Flock sur un lampadaire et un véhicule équipé d'un appareil de détection avancé. Des signaux lumineux illustrent les échanges de données sans fil sur fond sombre."
coverCaption: "Comment les changements de matériel Flock Safety déjouent les outils de détection open source, et comment la communauté les rattrape"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Si ton détecteur Flock-You reste silencieux sur un trajet où il repérait toujours des caméras, tu ne l'imagines pas et ton matériel n'est probablement pas en panne.** Le matériel et le firmware des caméras Flock Safety ont changé au moins deux fois au cours de la dernière année, ce qui a perturbé les méthodes de détection de la communauté. Les chercheurs open source ont dû reconstituer une nouvelle signature à chaque fois.

*La situation évolue vite. La méthode de détection et la liste OUI ci-dessous reflètent la branche `main` de `colonelpanichacks/flock-you` en septembre 2026. Consulte le [dépôt GitHub](https://github.com/colonelpanichacks/flock-you) avant de conclure que ton appareil est défectueux.*

{{< youtube id="cVf-id71BuQ" >}}

*La vidéo de Valleytech Custom Solutions illustre le symptôme décrit : un trajet courant de détection WiFi en déplacement ne renvoie soudainement aucune détection sur plusieurs versions du firmware, alors que les caméras étaient repérées de façon fiable sur ce trajet et que certaines caméras signalées avaient physiquement disparu du comté.*

______

## Un trajet de détection mobile qui ne trouve soudain plus rien

Les signalements décrivent souvent le même scénario. Une personne emprunte un itinéraire qu'elle a déjà parcouru des dizaines de fois. Son détecteur dispose du firmware actuel et repérait auparavant les mêmes caméras. Lors d'un trajet, plus rien : ni bip ni entrée de journal, avec toutes les compilations personnalisées testées.

La vidéo de Valleytech raconte un cas similaire : le trajet quotidien jusqu'au bureau de poste détectait toujours au moins une caméra Flock, mais plus aucune maintenant. Sur un deuxième trajet près de Micro Center, cinq caméras apparaissaient auparavant. Une seule reste active, les quatre autres ont été arrachées de leurs poteaux.

**Deux phénomènes faciles à confondre se produisaient sur la même période :**

- **Certaines caméras sont retirées ou déplacées physiquement**, ce qui réduit réellement le nombre d'appareils à détecter.
- **La signature sans fil des caméras a changé**, et une caméra encore sur son poteau peut donc ne plus déclencher un appareil au firmware ancien.

Deux tickets GitHub du dépôt `colonelpanichacks/flock-you`, ouverts à quelques mois d'intervalle, documentent le deuxième problème. Ensemble, ils montrent que la communauté a déjà dû faire évoluer la méthode de détection deux fois.

______

## Ticket #20 : le point d'accès de gestion a cessé d'émettre

**[Le ticket #20](https://github.com/colonelpanichacks/flock-you/issues/20)** a été ouvert en janvier 2026. Une personne a testé son appareil à côté d'une caméra Flock connue et répertoriée sur DeFlock, mais n'a rien détecté. Au cours des semaines suivantes, d'autres personnes ont signalé le même résultat depuis la Floride, l'Indiana, Atlanta et le Midwest, avec du matériel et des antennes différents.

Un commentaire a posé la question essentielle : **Flock avait-il modifié quelque chose de son côté, interrompant la détection pour tout le monde à peu près au même moment ?**

Le responsable du projet, colonelpanichacks, a fini par le confirmer. **Vers décembre 2025, Flock a désactivé le point d'accès de gestion utilisé par ses caméras pour émettre.** Ce point d'accès constituait la base initiale de la détection sans fil. À sa disparition, la communauté s'est tournée vers les signaux Bluetooth Low Energy (BLE). Cette solution de remplacement est aussi devenue peu fiable au printemps 2026.

| Surface de détection | État |
|---|---|
| **Point d'accès WiFi de gestion** | Désactivé par Flock vers décembre 2025 |
| **Balises BLE** | Détection peu fiable depuis le printemps 2026 |
| **Liaison cellulaire LTE** | Toujours utilisée pour les téléversements vers le cloud, mais indétectable passivement |
| **Requêtes probe 802.11 wildcard** | Base actuelle de la détection (voir ci-dessous) |

*Tout firmware personnalisé fondé sur les anciennes méthodes de détection par point d'accès ou BLE cherche maintenant un signal que les caméras n'émettent plus. Voilà pourquoi un appareil qui fonctionnait se tait soudainement sans que son matériel soit en cause.*

______

## Méthode de remplacement : requêtes wildcard et fingerprinting des trames

Le firmware actuel de `flock-you` fonctionne en mode promiscuous 802.11 dédié. La radio n'émet jamais et ne rejoint aucun réseau. Elle écoute seulement, en passant sur les canaux WiFi 11, 6 et 1 pendant 250 millisecondes chacun, pour suivre les changements de canal fréquents des caméras.

**Le firmware ne déclenche une alerte que si toutes les conditions suivantes sont réunies :**

1. La trame est une **requête probe de gestion 802.11** (type 0, sous-type 4).
2. L'**élément d'information SSID est présent et sa longueur est égale à 0**. Il s'agit donc d'une requête wildcard, et non d'une recherche pour un réseau donné.
3. L'adresse de l'émetteur (**addr2**) correspond à l'un des préfixes OUI Flock connus.
4. Les autres éléments d'information de la trame correspondent à l'empreinte documentée par la communauté DeFlockJoplin, fondée sur les travaux de Pintor et Atzori publiés en 2022 sur le **[fingerprinting des éléments d'information des requêtes probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

Le firmware nomme cette méthode `wifi_wildcard_probe_ie_sig`. Lors de tests sur le terrain, la communauté DeFlockJoplin a repéré **11 caméras connues sur 12 avec seulement 2 faux positifs** sur son itinéraire de test. C'est la même référence validée sur le terrain que celle citée dans le **[guide matériel](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** du projet. L'OUI de la douzième caméra a depuis été ajouté à la liste ci-dessous.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Chronologie de l'évolution des méthodes de détection des caméras Flock : point d'accès WiFi de gestion, balises Bluetooth Low Energy, requêtes probe wildcard et fingerprinting des éléments d'information, puis nouveaux SSID, 5 GHz et contournement par adresse MAC" >}}

______

## Liste OUI actuelle

L'empreinte wildcard-probe ne se déclenche que si l'adresse MAC de l'émetteur correspond à un préfixe OUI confirmé par la communauté sur du matériel Flock réel. La liste est principalement tenue par le chercheur **@NitekryDPaul**. La communauté **DeFlockJoplin** a ajouté le 31e préfixe après avoir repéré une caméra absente de la liste initiale de 30 éléments.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Cette liste n'est pas statique.** Les notes de recherche mentionnent plusieurs préfixes testés puis rétrogradés. L'un appartenait à un lecteur multimédia Sony, un autre était un marqueur provisoire qui ne correspondait à rien. Deux entrées sont considérées comme peu fiables. Le préfixe `82:6b:f2` est conservé malgré son statut d'adresse administrée localement, car son exclusion aurait supprimé discrètement une détection réelle confirmée par DeFlockJoplin.

**Un préfixe a désormais été confirmé indépendamment sur du matériel en service municipal.** L'unité Flock dont les images du système de fichiers ont été publiées en septembre 2026 portait l'adresse MAC **`f4:6a:dd:57:46:fb`**; le préfixe `f4:6a:dd` apparaît en treizième position dans la liste. Ce n'était ni un appareil de laboratoire ni un exemplaire acheté. La caméra était fixée à un poteau à Wauwatosa, dans le Wisconsin, et photographiait la circulation. C'est la confirmation individuelle la plus solide obtenue pour un préfixe de cette liste.

*Si tu entretiens un fork du firmware, récupère la liste OUI depuis le répertoire `datasets/` du projet amont au lieu d'en intégrer une copie codée en dur. La liste évolue avec la recherche; une copie obsolète peut te faire manquer des caméras sans que tu le remarques.*

______

## Classement des signaux de détection

Le firmware actuel s'appuie surtout sur la correspondance OUI, qui est le plus faible des cinq signaux disponibles. La communauté de **[WiFi Mothership](https://wifimothership.com/flock)** les classe par niveau de confiance en s'appuyant sur les recherches firmware de GainSec.

| Confiance | Signal | Notes |
|---|---|---|
| **ÉLEVÉE** | **Identifiant fabricant BLE `0x09C8`** (XUNTONG) | Empreinte numérique la plus forte. Présente sur les unités Raven et les Falcon ou Sparrow équipés d'un module de batterie |
| **ÉLEVÉE** | **UUID des services BLE Raven de `0x3100` à `0x3500`** | Services GATT propres à Raven pour le GPS, l'alimentation, le réseau, le téléversement et les erreurs. Détection limitée au matériel Raven |
| **MOYENNE** | **Motif SSID WiFi `^Flock-[A-Z0-9]+$`** | Nom par défaut du point d'accès de configuration. Le firmware contient aussi les SSID `FS Ext Battery`, `Penguin` et `Pigvision` |
| **MOYENNE** | **Sous-chaîne du nom d'appareil BLE** | Des noms tels que `FS Ext Battery` apparaissent dans les données publicitaires sans analyse des données fabricant |
| **FAIBLE** | **Correspondance MAC et préfixe OUI** | **Méthode la plus bruyante.** Les préfixes des fournisseurs de composants apparaissent dans des milliers de produits sans rapport |

*La dernière ligne est celle dont le firmware actuel dépend le plus, ce qui constitue le problème central d'une détection fondée d'abord sur les OUI.*

### Pourquoi la liste OUI est si bruyante

Les 31 préfixes de la liste ne représentent pas 31 identifiants Flock. WiFi Mothership suit en parallèle **26 préfixes et classe chacun selon son propriétaire réel**.

| Catégorie | Nombre | Propriétaire |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, attribution IEEE à l'entreprise elle-même |
| **Modules de batterie** | 10 | Composants Silicon Labs dans les blocs-batteries étendus |
| **Modules de caméra** | 11 | Modules WiFi de caméras Liteon Technology |
| **Infrastructure informatique** | 4 | Raspberry Pi Foundation et Raspberry Pi Trading |

**Vingt-cinq de ces 26 préfixes appartiennent à des fournisseurs de composants**, utilisés en très grandes quantités dans du matériel sans lien avec Flock. Un préfixe de batterie Silicon Labs ou de module caméra Liteon apparaît dans des produits sans rapport avec Flock Safety, et les cartes Raspberry Pi sont répandues.

**Une correspondance est un indice, pas une identification.** C'est pourquoi la signature wildcard-probe compte autant : combinée à une OUI, une requête probe avec SSID vide fait passer le niveau de confiance d'une supposition à 62 sur l'échelle du projet.

*Seul `B4:1E:52` suffit à répondre à la question « est-ce un appareil Flock ? ». Les 30 autres préfixes sont des indices secondaires.*

### Combien de caméras exposent un point d'accès

Les données de détection en déplacement donnent un minimum. WiFi Mothership a recensé **au moins 900 points d'accès Flock sur WiGLE en 2025**. Un point d'accès Flock correspond à un appareil qui diffuse le SSID de configuration par défaut `Flock-XXXX`.

Ce chiffre décrit les appareils qui exposent un point d'accès de configuration, pas le parc installé. Flock revendique des dizaines de milliers de caméras et la plupart n'émettent rien qu'une personne passant en voiture puisse enregistrer. **La carte est un échantillon, et un petit échantillon.**

______

## Ticket #43 : nouveau motif SSID, 5 GHz et anti-fingerprinting MAC

Trois mois après la clôture du ticket #20, un second signalement a décrit une possible contre-mesure délibérée plutôt qu'un changement fortuit du firmware. **[Le ticket #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, déposé en mai 2026, s'appuie sur des données WiGLE recueillies près d'une caméra déjà confirmée sur DeFlock. Il documente trois éléments auxquels les outils existants n'étaient pas préparés.

### Constat 1 : un autre format SSID

Le point d'accès Flock documenté suivait toujours le motif `Flock-XXXXXX`. La caméra de ce signalement diffusait **`Flock Camera net.`**, une convention de nommage complètement différente. Toute personne recherchant le caractère générique `Flock-*` sur WiGLE, comme plusieurs chercheurs le faisaient, n'aurait obtenu aucun résultat pour cette caméra pourtant active.

### Constat 2 : point d'accès 5 GHz confirmé

La même caméra diffusait simultanément sur le **canal 1 à 2,4 GHz** et le **canal 157 à 5 GHz**, avec des adresses MAC consécutives sur chaque bande (`...9f:a2:de` et `...9f:a2:df`). Cela indique un seul module WiFi double bande attribuant des adresses adjacentes à chacune de ses radios, plutôt que deux appareils distincts. Un signalement indépendant du chercheur nsm_barii avait déjà enregistré une requête probe Flock sur le canal 149 à 5 GHz. Il existe donc maintenant deux observations confirmant que le 5 GHz est bien utilisé.

**Toutes les méthodes de détection décrites plus haut, y compris le firmware actuel fondé sur les requêtes wildcard, n'écoutent qu'à 2,4 GHz.** Une caméra qui diffuse uniquement ou surtout à 5 GHz reste invisible pour ce matériel, même si la liste OUI est exacte.

### Constat 3 : adresses MAC administrées localement sur le point d'accès

Les deux adresses MAC capturées ont le **bit d'administration locale activé**. Elles ne proviennent donc pas du bloc OUI de Flock enregistré auprès de l'IEEE. La logique standard de détection de `flock-you` ignore volontairement les adresses administrées localement, car c'est la méthode habituelle pour filtrer les téléphones et ordinateurs portables qui randomisent leur MAC.

**Ce filtre réduit les faux positifs, mais écarte aussi une caméra Flock qui utilise une MAC administrée localement sur son interface de point d'accès.** Les derniers octets consécutifs des deux adresses capturées écartent une génération aléatoire et suggèrent une attribution structurée.

| Constat | Ce qui fonctionne encore |
|---|---|
| **Nouveau format SSID** (`Flock Camera net.`) | La détection par motif SSID fonctionne si l'on élargit le motif |
| **Fonctionnement à 5 GHz** | Rien dans le firmware WiFi actuel, qui ne scanne que le 2,4 GHz |
| **MAC administrée localement** | La détection par motif SSID, qui ne dépend pas de l'adresse MAC |

*La correspondance SSID est la seule méthode du tableau qui reste efficace quelle que soit la bande ou la manière dont l'adresse MAC est attribuée. C'est une raison pratique d'ajouter des motifs SSID plus larges plutôt que de compter uniquement sur les correspondances OUI.*

______

## Flock cherche-t-il délibérément à échapper à la détection ?

Aucun des deux tickets GitHub ne prouve une intention. L'auteur du ticket #43 a lui-même posé la question sans y répondre : ce comportement se retrouve-t-il dans les déploiements Flock ou concerne-t-il une seule version du firmware sur une seule caméra ?

Considère les deux tickets ensemble. Une surface de détection disparaît, la communauté trouve un remplacement, et les angles morts de ce remplacement (analyse limitée à 2,4 GHz, correspondances OUI et filtrage des MAC administrées localement) correspondent aux caractéristiques qu'un nouveau SSID, une radio 5 GHz et une adresse MAC administrée localement pourraient exploiter. **Il peut s'agir d'une coïncidence due à un cycle de mise à jour du firmware sans rapport. Il peut aussi s'agir d'un fournisseur qui réduit sa présence sans fil, rendant la détection tierce plus difficile, volontairement ou non.**

*La meilleure approche n'est pas de trancher. Il faut construire une détection qui ne repose pas sur une seule hypothèse, puisque l'historique de deux ans de ce projet montre qu'aucune n'est restée valable indéfiniment.*

### Confirmation visuelle : caméra sous tension, sans émission

**[Une troisième courte vidéo de Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) examine l'hypothèse d'une caméra retirée.**

{{< youtube id="sjI8FB0cLk0" >}}

Le créateur est retourné de nuit à la caméra de la première vidéo et a confirmé visuellement que les **LED IR étaient toujours allumées** : l'appareil était alimenté et éclairait la scène pour les prises nocturnes. En même temps, **tous les firmwares personnalisés testés ont enregistré zéro détection légitime**. Une alerte s'est déclenchée, mais il s'agissait d'un faux positif confirmé. La caméra n'émettait rien sur le réseau sans fil.

**Cela permet de distinguer clairement les deux explications possibles.** Une caméra arrachée ou déplacée n'explique pas un appareil visiblement alimenté et éclairant la nuit. Une caméra active et éclairée, mais silencieuse pour toutes les méthodes WiFi, indique la disparition de sa signature sans fil, pas celle du matériel.

Après avoir échangé avec d'autres développeurs travaillant sur le même problème, le créateur a signalé que ce résultat n'était pas isolé. **Plusieurs personnes ont observé le même phénomène à peu près au même moment**, ce qui suggère un changement coordonné de Flock à l'échelle nationale plutôt qu'une anomalie locale. *Cette affirmation est anecdotique et repose sur des échanges informels, pas sur un jeu de données publié. Elle correspond néanmoins aux périodes de décembre 2025 et du printemps 2026 décrites dans le ticket #20. Un nouveau ticket GitHub serait le bon endroit pour la consigner.*

______

## Ce que cela signifie pour ton matériel de détection

Si ton appareil est devenu silencieux, vérifie ces points avant de conclure qu'il est en panne :

1. **Mets d'abord le firmware à jour.** Si tu utilises une version antérieure à la branche `main` actuelle, tu cherches probablement encore le point d'accès de gestion désactivé ou les balises BLE devenues peu fiables. Télécharge le dernier firmware et réinstalle-le.
2. **Vérifie que la caméra est toujours là.** Certains signalements sans détection concernaient du matériel réellement arraché ou déplacé, pas une panne de détection. Compare avec **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** ou **[DeFlock](https://deflock.org/)** avant de dépanner ton appareil.
3. **Ralentis aux intersections.** Une durée de présence de 250 ms par canal peut te faire dépasser la fenêtre de détection avant que la radio n'atteigne le bon canal. Un arrêt de 30 à 60 secondes détecte davantage de caméras qu'un passage rapide avec une antenne plus grande.
4. **Signale tes observations.** Zéro détection à côté d'une caméra confirmée visuellement est exactement le type d'information qui a conduit aux tickets #20 et #43. Ouvre un nouveau ticket au lieu de supposer que quelqu'un d'autre l'a déjà signalé.
5. **Connais les limites actuelles.** Un firmware uniquement WiFi à 2,4 GHz ne détectera pas une caméra passée au 5 GHz ou silencieuse sur les bandes analysées. C'est une lacune réelle, pas un défaut de ta compilation.

**Le matériel n'est pas inutile pour autant.** La liste OUI et l'empreinte wildcard-probe repèrent toujours la grande majorité des caméras déployées. Considère chaque détecteur, construit soi-même ou acheté, comme un instantané d'une course continue, pas comme une solution permanente.

{{< stscollective-ad "flockyou" >}}

______

## Une approche parallèle : détecter le flash infrarouge plutôt que le signal WiFi

La détection sans fil n'est pas le seul front de cette course. **[Une autre vidéo de suivi](https://www.youtube.com/shorts/mzpr6bslsYA) du même créateur, Valleytech Custom Solutions, décrit une approche complètement différente** : observer l'illuminateur infrarouge de la caméra plutôt que d'écouter une signature radio.

{{< youtube id="mzpr6bslsYA" >}}

La plupart des caméras ALPR, y compris celles de Flock, utilisent **un éclairage infrarouge pour capturer des plaques lisibles la nuit**, comme les caméras de sécurité ordinaires qui fonctionnent dans l'obscurité. La lumière IR est invisible à l'œil humain, mais un capteur d'image dépourvu de filtre IR-Cut peut la voir. *L'absence de ce filtre transforme un module caméra ordinaire en détecteur Flock.*

### À quoi ressemble le prototype

L'approche décrite dans la vidéo a connu plusieurs versions avant d'aboutir à une combinaison exploitable :

- **Première tentative** : récepteurs à photodiodes IR dédiés. Ils fonctionnaient, mais les composants étaient trop chers pour une solution DIY pratique.
- **Deuxième tentative** : **Jetson Nano avec un module caméra Raspberry Pi**. Cela a démontré la faisabilité, mais le coût et la consommation électrique rendaient le système peu pratique à tenir en main ou à installer dans un véhicule.
- **Montage actuel** : **module caméra ESP32 sans objectif IR-Cut**. Le créateur a testé **ESP32-CAM** et **M5Stack S3 Cam** avant de choisir **Seeed Studio XIAO ESP32S3 Sense**, associé à un **module GNSS Seeed XIAO fondé sur la puce Quectel L76K** pour géolocaliser les détections. Il reprend le même modèle de détection mobile GPS que le tableau de bord WiFi de `flock-you`.

| Exigence | Pourquoi elle compte |
|---|---|
| **Module caméra sans filtre IR-Cut** | Le filtre qui rend les couleurs des photos normales bloque précisément la lumière dont cette méthode a besoin |
| **Une caméra plutôt qu'une photodiode** | Les récepteurs à photodiodes capables d'isoler le signal étaient trop chers pour un montage DIY pratique |
| **Journalisation GPS** | Associe les détections à un emplacement, comme le tableau de bord Flask du firmware WiFi |

### Le rythme de clignotement de la caméra

L'hypothèse repose sur un illuminateur qui clignote de manière répétée et détectable plutôt que de rester allumé. Le créateur a rapporté une **mesure personnelle d'environ 20 millisecondes allumé et 80 millisecondes éteint, soit une période de 100 millisecondes, un rapport cyclique de 20 % à 10 Hz**. Il a précisé que cette valeur n'est pas vérifiée et peut être erronée. *Utilise-la comme point de départ de tes propres mesures, pas comme une spécification confirmée. Flock ne l'a pas publiée et le créateur n'affirme pas en être sûr.*

### État du projet

**Il s'agit d'un premier prototype DIY, pas d'un produit fini.** Le créateur décrit le logiciel comme « vibe coded » et toujours en cours de développement. Un buzzer pour les alertes sonores est prévu mais pas encore ajouté. Il n'existe pas non plus de carte prête à l'emploi comparable à l'OUI-SPY. La version actuelle nécessite toujours qu'**une personne confirme visuellement** qu'une détection signalée est bien une caméra et non une autre source infrarouge. Elle sert d'outil de présélection, pas de système entièrement automatisé.

*Cette surface de détection est différente de toutes les autres de l'article. Elle ne dépend ni du WiFi, ni de la bande 2,4 ou 5 GHz, ni des correspondances OUI, ni du comportement des adresses MAC. Les techniques d'évasion du ticket #43 ne la concernent donc pas. Elle a ses propres limites : visibilité directe, interférences de la lumière du jour et rapport cyclique non confirmé de manière indépendante.*

______

## Ce que fait la communauté

La réponse aux deux tickets a suivi le modèle qui rend le projet utile depuis deux ans : une personne signale une lacune, une autre contribue à un correctif et celui-ci est publié dans une mise à jour au lieu de rester dans un arriéré.

- **Le ticket #20** s'est conclu par une cause confirmée et une réécriture du firmware autour de la signature wildcard-probe, grâce aux recherches sur le terrain de la communauté DeFlockJoplin.
- **Le ticket #43** est toujours ouvert au moment de la rédaction; la suggestion d'ajouter une correspondance de motif SSID n'a pas encore été mise en œuvre. *Ajouter `Flock Camera` comme motif supplémentaire est une contribution limitée et bien définie pour qui connaît la logique de correspondance du firmware.*
- Le jeu de données OUI est versionné et daté. Les entrées rétrogradées ou peu fiables sont documentées au lieu d'être supprimées discrètement, afin que les personnes qui créent un fork sachent ce qui a changé et pourquoi.

*C'est l'avantage pratique des outils de détection open source par rapport à une solution fermée. La personne qui découvre une lacune ne peut pas corriger un détecteur propriétaire. Ce projet a déjà été corrigé deux fois.*

______

## L'autre réponse : retirer le matériel

La détection sans fil est une réaction à ces caméras. Une autre initiative s'est attaquée au matériel lui-même et, en septembre 2026, a produit les preuves publiques les plus détaillées sur le fonctionnement interne d'une caméra Flock.

**Le collectif stegan0gram a retiré une caméra de son poteau, copié le stockage interne et publié les images du système de fichiers via Distributed Denial of Secrets.** Il a décrit son travail ainsi :

> « Pourquoi simplement les détruire alors que nous pouvons les désosser et découvrir les secrets de ceux qui nous espionnent ? Nous avons libéré le matériel sur le terrain, l'avons désarmé, puis avons procédé à l'ingénierie inverse des caméras et du matériel solaire associé. »

*La distinction compte. Détruire une caméra retire une unité. La rétro-ingénierie apporte des preuves sur l'ensemble du parc.*

### Ce que le retrait a révélé

Le jeu de données publié comprend une **partition multimédia de 18 Go**, une **image système Android de 1,5 Go** et une **partition d'identifiants de 32 Mo**, ainsi que la clé récupérée pour le conteneur multimédia chiffré. Les chercheurs ont déterminé les versions du système d'exploitation et du noyau, des identifiants backend codés en dur et des jetons d'authentification en texte clair stockés par la caméra.

Ces preuves étayent les recherches de sécurité présentées dans **[Vulnérabilités des caméras Flock Safety : plus de 50 failles découvertes](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, qui reposaient jusque-là sur des appareils de laboratoire et des exemplaires achetés.

### Les suites du retrait

Les interventions physiques ont des conséquences, et le bilan est contrasté :

- **Plusieurs personnes ont été arrêtées dans tout le pays** pour avoir prétendument saboté des caméras Flock.
- **Certaines municipalités ont annoncé qu'elles cesseraient d'utiliser les caméras Flock.** C'est le résultat recherché par leurs opposants.
- **Un service de police a fabriqué un faux boîtier de caméra Flock imprimé en 3D** pour attirer et arrêter d'éventuels vandales.

Noel Pichardo, ancien policier de Pawtucket, dans le Rhode Island, est devenu critique de Flock après avoir contesté l'utilisation des caméras par son service. Il a déclaré à WIRED comprendre la frustration, mais craindre que le sabotage ne renforce la conviction de la police et du gouvernement que cette technologie est nécessaire. « Plus le gouvernement ignore les plaintes des habitants opposés à ce type de surveillance, plus cela se produira », a-t-il affirmé.

### La place de la détection

Le démontage ne change rien au problème de détection traité dans cet article. La caméra émet toujours, le firmware a toujours besoin de sa liste OUI et de sa signature probe, et les deux pannes documentées restent d'actualité.

L'extraction confirme **l'identité du matériel**, notamment un préfixe OUI vérifié sur un appareil réel, et rappelle quel type de pression modifie les déploiements. **Les caméras quittent un itinéraire parce qu'un conseil municipal met fin à un contrat, pas parce qu'un détecteur se tait.** Les outils sans fil répondent à une question personnelle sur ton environnement. Le débat politique répond à la question plus large, et l'extraction lui a fourni les preuves les plus solides à ce jour.

______

## Conclusion : la détection reste une cible mouvante

Un détecteur silencieux sur un itinéraire où il trouvait des caméras ne prouve pas que le matériel est en panne. C'est un indice que la signature sans fil qu'il reconnaît a de nouveau changé, pour la deuxième fois en un an. **Le point d'accès de gestion, les balises BLE et peut-être maintenant les hypothèses « 2,4 GHz uniquement » et « OUI uniquement » du firmware actuel** ont tous eu une durée de vie limitée.

**La solution n'a jamais été d'abandonner la détection sans fil.** Elle consiste à garder visibles et documentées les hypothèses de la méthode afin de les corriger quand un signalement comme le ticket #20 ou #43 apparaît. C'est l'intérêt d'un firmware open source par rapport à une solution fermée : la communauté peut corriger la lacune dès qu'elle la découvre, sans attendre le fournisseur.

### Points clés

- **Deux surfaces de détection documentées ont déjà disparu** : le point d'accès WiFi de gestion (désactivé vers décembre 2025) et les balises BLE (peu fiables depuis le printemps 2026).
- **La méthode actuelle, requêtes wildcard, correspondance OUI et fingerprinting IE, a repéré 11 caméras sur 12 lors de tests sur le terrain**, mais ne fonctionne qu'en WiFi à 2,4 GHz.
- **Un signalement en attente décrit un nouveau format SSID, un point d'accès 5 GHz confirmé et des MAC administrées localement**, que la méthode actuelle limitée aux OUI et au 2,4 GHz ne peut pas voir.
- **Une méthode sans fil parallèle apparaît** : un module caméra ESP32 sans filtre IR-Cut repère l'illuminateur infrarouge de Flock et échappe aux techniques d'évasion sans fil décrites.
- **La confirmation visuelle étaye l'absence de signal sans fil** : une caméra était visiblement allumée et éclairait la nuit, mais a enregistré zéro détection WiFi légitime. Pour cette unité, le retrait n'explique pas le silence.
- **Zéro détection près d'une caméra connue ne signifie pas automatiquement que ton matériel est en panne.** Mets d'abord le firmware à jour, puis vérifie que la caméra est toujours là.
- **Le projet open source publie des corrections lorsque la communauté repère des lacunes.** Consulte les tickets GitHub, pas seulement le README, pour connaître l'état actuel.

### Étapes suivantes

1. **Mets le firmware à jour** vers la branche `main` actuelle avant de dépanner autre chose : **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Lis le guide matériel complet** si tu ne le connais pas encore : **[Projet de détection Flock-You : guide matériel de contre-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Compare les zones supposées sans détection** avec **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** avant de conclure que ton appareil a manqué quelque chose.
4. **Comprends le système auquel tu fais face** : **[Surveillance par caméras Flock Safety : ampleur, enjeux de confidentialité et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Associe détection WiFi et détection cellulaire** avec **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** pour une vision plus complète. Aucune méthode de cet article ne détecte les simulateurs de stations de base cellulaires.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acheter des appareils FlockYou prêts à l'emploi, économiser 20 %
{{< /centerbutton >}}

______

## Articles associés

| Article | Contenu |
|---|---|
| **[Projet de détection Flock-You : guide matériel de contre-surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guide technique des trois plateformes matérielles, de la configuration du firmware et de la méthode de détection présentée ici |
| **[Flock Finder : cartographier les caméras Flock présumées près de chez toi](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Comparer une zone supposée sans détection à plus de 40 000 emplacements de caméras cartographiés avant de dépanner ton appareil |
| **[Caméras Flock : outil de sécurité publique ou système de surveillance sans mandat ?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analyse des possibilités offertes par la base de données Flock et des raisons pour lesquelles la question du mandat compte davantage que la détection |
| **[Surveillance par caméras Flock Safety : ampleur, enjeux de confidentialité et stratégies de protection](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Ampleur du déploiement, cas d'abus documentés et ressources d'organisation communautaire |
| **[Vulnérabilités des caméras Flock Safety : plus de 50 failles découvertes](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Recherche sur le matériel et les logiciels, distincte de la détection sans fil |
| **[Flasher les appareils Rayhunter : guide complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Détecter les IMSI catchers et les stingrays, l'équivalent cellulaire de la lacune WiFi décrite ici |

______

## Références

1. [Dépôt GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Ticket GitHub #20 - Caméras Flock non détectées, autres appareils détectés](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [Ticket GitHub #43 - Signal 5 GHz ? Nouvel OUI / filtrage des adresses MAC](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Jeu de données de recherche OUI de NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - Recherche ALPR de la communauté](https://deflockjoplin.today)
7. [Pintor, L. et Atzori, L. (2022) - Analyse des requêtes probe Wi-Fi pour le fingerprinting des éléments d'information, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED et 404 Media - Des pirates sont entrés dans une caméra Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Les caméras Flock présentent de nombreuses vulnérabilités et des identifiants codés en dur](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Images du système de fichiers d'une caméra ALPR Flock](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Cette semaine en sécurité : les caméras Flock sont anciennes, correctifs Microsoft et attaques SSH](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Référence et détection des appareils ALPR Flock Safety](https://wifimothership.com/flock)
13. [GainSec - Recherche sur le firmware et avis de sécurité](https://gainsec.com/)
14. [The Hunt for the Hidden Probe - Comportement des requêtes wildcard pour SSID masqué](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
15. [DeFlock - Carte collaborative des caméras ALPR](https://deflock.org/)
16. [Colonel Panic Tech - OUI-SPY et matériel de détection](https://colonelpanic.tech)
17. [STS Collective - Appareils FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
18. [Il se passe quelque chose d'étrange avec les caméras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
19. [Détection mobile infrarouge des caméras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
20. [Caméras Flock toujours allumées mais sans émission - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
21. [Reconnaissance automatique des plaques d'immatriculation - Wikipédia (éclairage infrarouge en ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
22. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
23. [Module GNSS L76K pour Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
