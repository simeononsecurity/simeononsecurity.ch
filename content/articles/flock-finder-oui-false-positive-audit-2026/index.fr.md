---
title: "Nous avons cartographié 146 526 « caméras Flock ». 50 278 étaient des systèmes ClickShare"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "L’audit de Flock Finder révèle ClickShare et d’autres faux positifs, explique les preuves et documente les corrections."
genre: ["Recherche en sécurité", "Technologies de confidentialité", "Projets open source", "Journalisme de données", "Contre-surveillance"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Empreinte OUI", "WiGLE", "Faux positifs", "Qualité des données", "Barco ClickShare", "Adresse MAC", "OUI IEEE", "Empreinte des éléments d’information", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Responsabilité open source", "Cartographie de la surveillance", "WiFi", "Requête de sondage", "Randomisation MAC"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Une carte urbaine sombre couverte de repères rouges qui désignent des appareils WiFi de bureau, tandis que quelques repères verts restent des détections plus solides"
coverCaption: "L’audit de 146 526 enregistrements Flock Finder a montré comment une observation de terrain utile est devenue une affirmation cartographique trop catégorique."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Nous avons placé 146 526 points sur une carte de caméras de surveillance. Au moins 50 278 étaient des systèmes de présentation Barco ClickShare. Le matériel de salle de conférence représentait plus d’un tiers de ce que notre titre appelait « caméras cartographiées ».**

C’était notre projet, notre pipeline de données et notre erreur. Flock Finder interrogeait chaque jour WiGLE sur les préfixes d’adresses MAC observés sur les caméras Flock Safety, publiait les résultats avec des coordonnées précises et affichait tous les résultats avec le même repère. Les métadonnées contenaient le mot `suspected` et la documentation signalait les faux positifs. La carte et le titre exprimaient pourtant une certitude.

**Résultat pour le lecteur :** reproduisez l’audit, distinguez observation et attribution, et affichez le degré de confiance avec le repère et le titre. Une correspondance de préfixe sert à enquêter, elle ne prouve pas qu’il s’agit d’une caméra.

Quand nous avons calculé un histogramme de la colonne SSID, le jeu de données a révélé le problème en quelques minutes. ClickShare n’était que la catégorie la plus importante. 6 099 autres enregistrements s’appelaient `SMARTGATE_*` , 3 801 commençaient par le préfixe générique WiFi Direct `DIRECT-` , 314 portaient exactement le nom `AndroidAP` , 138 indiquaient `Audi HUD` , 133 `MAX-PRINTER` , et 30 contenaient le verdict d’un autre détecteur. Au total, **60 793 lignes, soit 41,5 %, respectaient les règles de nommage des autres appareils connues dans l’audit initial.**

Flock Finder publie désormais une classe de preuve par enregistrement, exclut par défaut les appareils connus comme étrangers de la carte et du titre, propose des filtres, signale les enregistrements hors du marché principal et sépare les préfixes à forte confiance de ceux des fabricants sous contrat. Cet article décrit l’erreur, les preuves et les limites restantes.

______

## Comment fonctionne la détection communautaire des ALPR

Les détecteurs Flock créés par la communauté combinent généralement trois types de preuves sans fil :

1. **Préfixes WiFi MAC/OUI.** Les premiers octets d’une adresse MAC administrée mondialement peuvent identifier l’organisation à laquelle le bloc d’adresses a été attribué.
2. **Comportement WiFi.** Un SSID, une requête de sondage générique, l’adresse du destinataire, un motif de canaux ou une séquence d’éléments d’information 802.11 peut préciser la classe d’appareil.
3. **Preuves Bluetooth.** Les identifiants de fabricant et les UUID de service peuvent identifier les radios exposées par un produit ou une génération de micrologiciel.

La correspondance OUI s’est répandue, car elle est peu coûteuse et passive. Un ESP32 abordable peut examiner les trames 802.11 proches sans se connecter à un réseau. Une base historique comme [WiGLE](https://wigle.net/) permet aussi de rechercher des observations antérieures sans déployer de scanners propres.

La méthode suit une filiation communautaire : cartographie et action locale de [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), forks et projets associés comme notre [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32), puis [Flock Finder](https://github.com/simeononsecurity/flock-finder), qui a appliqué la liste de préfixes aux données WiGLE à l’échelle mondiale.

Le travail de terrain d’origine mérite un crédit clair. [@NitekryDPaul](https://github.com/NitekryDPaul) a observé 30 préfixes sur du matériel Flock réel grâce à des recherches en mode promiscuous. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) en a ajouté un pendant des essais sur le terrain. Ces observations étaient légitimes. Notre erreur a été de traiter **« observé sur une caméra Flock » comme si cela signifiait « exclusif aux caméras Flock ».**

______

## Le défaut structurel : un OUI décrit la chaîne d’approvisionnement

IEEE décrit un OUI comme un identifiant de 24 bits attribué à un fournisseur, fabricant ou autre organisation. Associé à 24 autres bits choisis par le bénéficiaire, il forme une adresse MAC. L’[IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) publie le registre.

Cela indique qui a reçu un bloc d’adresses. Cela ne révèle pas nécessairement la marque d’un produit fini. Les fabricants sous contrat construisent des modules radio pour plusieurs clients. Un fournisseur de puces peut ainsi apparaître dans des caméras, projecteurs, imprimantes, véhicules et cartes de loisir.

Les attributions du registre rendaient le risque visible :

| Titulaire | Préfixes dans la liste auditée |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` et autres |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Les entrées Espressif auraient dû nous alerter. Deux préfixes d’une prétendue liste de caméras appartenaient au fabricant de l’une des plateformes WiFi embarquées les plus courantes au monde, y compris le silicium utilisé par de nombreux détecteurs communautaires.

`B4:1E:52` est différent, car il est enregistré directement au nom de Flock Safety. Il avait été ajouté à la liste de 38 préfixes dans le commit audité, **mais n’avait pas encore été interrogé** : `scan_stats.json` indiquait 31 préfixes interrogés. C’était aussi le cas de six préfixes de batteries ajoutés récemment. L’instantané ne prouve donc pas si le préfixe propre à Flock est fréquent ou rare. Nous ne transformerons pas « non interrogé » en « zéro résultat ».

Le dépôt actuel contient 39 préfixes après l’ajout de `E0:0A:F6` pour correspondre au micrologiciel du détecteur. Le résumé d’analyse conservé indique encore des données pour 31 préfixes. Les nouvelles entrées attendent donc un recalcul complet et ne sont pas des préfixes dont le résultat nul est établi.

______

## Le jeu de données s’est audité lui-même

Chaque chiffre historique ci-dessous a été régénéré depuis `data/flock_cameras.csv` au commit Flock Finder [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829), avec `csv` et `collections.Counter` de la bibliothèque standard Python. Aucun nouvel essai routier n’était nécessaire. Les noms, la géographie et la composition des préfixes contredisaient déjà le titre. Les chiffres de l’implémentation corrigée proviennent du résumé `scan_stats.json` conservé dans le dépôt actuel.

### La géographie était un signal précoce

Sur 146 526 lignes, 75 818 se trouvaient aux États-Unis, 70 674 hors des États-Unis et 34 n’avaient pas de pays. L’Allemagne comptait 13 491 enregistrements, suivie du Canada (6 251), de la France (5 839), de la Grande-Bretagne (4 836), des Pays-Bas (4 636) et de la Suisse (4 515).

{{< figure src="flock-finder-us-non-us-split.webp" alt="Barre empilée montrant 75 818 enregistrements aux États-Unis, 70 674 hors des États-Unis et 34 sans valeur de pays" caption="L’histogramme des pays totalise 146 492, car 34 lignes ont un pays nul." >}}

La géographie sert au tri, pas de preuve. Flock décrit son réseau comme « nationwide » et indique relier des clients dans [49 États américains](https://www.flocksafety.com/flock-ecosystem). L’expansion internationale peut également modifier le périmètre du marché. Nous signalons donc les lignes hors marché pour examen au lieu de les supprimer ou de déclarer faux chaque enregistrement hors des États-Unis.

Une conclusion prudente suffit : près de la moitié des enregistrements se trouvaient hors du marché américain principal du projet. Sans autre signal, une correspondance OUI mondiale ne pouvait donc pas être jugée aussi plausible.

### Plus de 60 000 appareils se nommaient eux-mêmes

| Famille SSID dans l’audit initial | Enregistrements | Part | Indication du nom |
|---|---:|---:|---|
| Contient `ClickShare` | 50 278 | 34,3 % | Matériel de présentation sans fil Barco |
| `SMARTGATE_*` | 6 099 | 4,2 % | Famille de passerelles ou d’appareils de type OBD |
| `DIRECT-*` | 3 801 | 2,6 % | Appareils WiFi Direct comme imprimantes, téléviseurs et adaptateurs |
| Nom exact `AndroidAP` | 314 | 0,2 % | Points d’accès Android |
| Nom exact `Audi HUD` | 138 | 0,1 % | WiFi d’infodivertissement ou d’affichage tête haute Audi |
| Nom exact `MAX-PRINTER` | 133 | 0,1 % | Imprimantes de bureau |
| `Flock ALPR [...]` | 30 | <0,1 % | Verdict d’un autre détecteur enregistré comme SSID |
| **Total de l’audit initial** | **60 793** | **41,5 %** | Identifiables comme autre matériel ou sortie de détecteur |

La documentation de support Barco précise que le nom réseau par défaut d’une unité de base ClickShare est [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). C’est une confirmation de première main de la famille du produit, sans déduction depuis la géographie ou le registre fournisseur.

Le classificateur de production a depuis remplacé les contrôles de noms exacts par des expressions régulières insensibles à la casse. Il inclut ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER et les libellés de sortie de détecteur. Sur les mêmes 146 526 lignes, il détecte 629 variantes AndroidAP, 139 variantes Audi HUD et 134 variantes MAX-PRINTER. Le dépôt actuel indique donc **61 110 enregistrements `identified_other`**, un peu plus que les 60 793 de l’audit initial.

### Le signal de confirmation n’était que de 2,4 %

Seules **3 502 lignes** portaient un SSID authentique de type Flock. 24 964 autres n’avaient pas de SSID. Les autres enregistrements désignaient du matériel différent ou associaient une OUI à un nom non classé.

Les 3 502 lignes confirmées contenaient 161 variantes authentiques de SSID : 3 342 occurrences du nom simple `Flock`, 157 noms uniques de provisionnement `Flock-XXXXXX` ou `FLOCK-XXXXXX`, et trois autres noms contenant `flock`. Un ancien décompte de 166 variantes dans le README comprenait cinq chaînes d’annotation distinctes `Flock ALPR [...]`. Elles indiquent le détecteur, pas la caméra.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="Barre empilée à 100 % répartissant 146 526 enregistrements en 3 502 confirmés par SSID, 57 267 nommés non classés, 24 964 OUI masquées seules, 60 763 identifiés comme autres et 30 retours de détecteur" caption="L’ancien titre fusionnait cinq classes de preuve très différentes dans un seul compte." >}}

### La qualité des préfixes variait fortement

Le taux de faux positifs n’était pas uniforme. Certains préfixes conservaient un signal Flock utile . D’autres étaient dominés par des appareils de bureau ou grand public nommés.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Barres empilées horizontales pour 31 préfixes OUI : SSID Flock en vert, SSID connus comme autres en rouge, SSID masqués en gris clair et enregistrements non classés en gris foncé" caption="Les plus grands préfixes contenaient souvent le plus d’appareils connus comme autres. Comptes issus de l’instantané d’audit de 146 526 lignes." >}}

Comparez deux préfixes que l’ancienne carte étiquetait pareil :

- `70:C9:4E` comptait 495 lignes : 133 noms de type Flock et 29 noms connus comme autres.
- `74:4C:A1` comptait 11 872 lignes : 211 noms de type Flock et 8 385 noms connus comme autres.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Comparaison : préfixe 70 C9 4E avec 26,9 % de SSID Flock et 5,9 % connus comme autres , préfixe 74 4C A1 avec 1,8 % de SSID Flock et 70,6 % connus comme autres" caption="Une étiquette uniforme masquait des rapports signal/bruit opposés." >}}

Le même schéma apparaît dans les plus grands groupes : `F4:6A:DD` comptait 8 422 noms connus comme autres contre 327 noms Flock , `D0:39:57`, 8 270 contre 473 , et `E0:4F:43`, 6 238 noms connus comme autres contre 66 noms Flock. Le volume d’un préfixe ne prouvait pas la qualité.

______

## La boucle de rétroaction cachée dans 30 lignes

Trente enregistrements du Texas avaient des SSID qui étaient clairement la sortie d’un autre détecteur :

| Libellé du détecteur enregistré comme SSID | Confiance indiquée par l’outil | Enregistrements |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | faible | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | moyenne | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | faible | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | faible | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | faible | 1 |

L’outil à l’origine de 26 cas sur 30 indiquait une faible confiance. Un téléversement WiGLE a ensuite enregistré le verdict de l’outil dans le champ SSID. Notre pipeline a repéré le mot `Flock` et aurait pu traiter ce libellé comme une confirmation indépendante.

Trente lignes sont peu nombreuses statistiquement. Le mécanisme, lui, compte : les outils partageant une base participative peuvent intégrer les résultats des autres et transformer une supposition peu fiable en corroboration apparente. Le correctif exclut toute la forme `Flock ALPR [` avant de rechercher la sous-chaîne de confirmation `flock`.

______

## Notre erreur

Le titre du README annonçait **« Caméras cartographiées | 146 526 »**. La carte publiait des coordonnées à pleine précision et représentait chaque résultat par le même repère. Elle se mettait à jour selon un calendrier GitHub Actions, donnant à une heuristique faible l’apparence d’un inventaire entretenu.

Nous avions inclus des réserves. Chaque élément avait `match_confidence: "suspected"`. Le README mentionnait ClickShare comme appareil potentiellement présent à proximité, et le projet conservait une piste séparée pour les candidats découverts par SSID. Ces réserves ne régissaient ni le nombre, ni le repère, ni la vue par défaut que les lecteurs voyaient.

Nous exprimions des réserves dans le texte et affirmions un chiffre dans le titre. La carte faisait la déclaration.

Le plus évitable est que le micrologiciel de notre [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) séparait déjà les identifiants à forte confiance de ceux des fabricants sous contrat et plaçait les preuves faibles sous le seuil d’alerte. Le concept existait dans la même organisation, mais le pipeline cartographique ne l’a pas repris.

Nous avons trouvé l’ampleur de l’erreur en calculant un histogramme de notre propre colonne SSID. Cela a pris quelques minutes. Chaque jour, nous publiions 146 526 lignes de preuve contre notre présentation.

______

## Nos changements

Le correctif est intégré au modèle de données et à l’interface Flock Finder :

- **Preuve par enregistrement :** `ssid_confirmed`, `oui_high`, `oui_mfr` ou `identified_other`.
- **Niveaux OUI :** les préfixes sont séparés entre forte confiance observée sur le terrain et niveaux partagés de fabricants sous contrat.
- **Exclusion des appareils connus comme autres :** ClickShare, SmartGate, WiFi Direct, points d’accès Android, Audi HUD, MAX-PRINTER et SSID de sortie de détecteur sont exclus par défaut de la carte et du titre.
- **Incertitude visible :** couleurs des repères, fenêtres contextuelles, comptes et filtres indiquent la classe de preuve.
- **Signalement du marché :** les enregistrements hors du marché principal américain portent `out_of_market: true` et restent disponibles pour examen.
- **Titre détaillé :** 3 502 confirmés par SSID, 73 691 suspects via OUI de niveau supérieur, 8 223 suspects via OUI de fabricants sous contrat et 61 110 identifiés comme autres.

Le chiffre corrigé utile à l’action est **85 416**, et il comprend encore 81 914 correspondances OUI non confirmées. C’est un décompte défendable de ce qui respecte les règles actuelles, pas un inventaire vérifié de caméras.

`identified_other` est aussi un classificateur opérationnel, pas un oracle. ClickShare dispose d’une documentation de première main solide sur son SSID par défaut, tandis qu’un motif général comme `DIRECT-` décrit une convention de nommage WiFi Direct partagée par de nombreux produits. La publication de la règle de correspondance et du champ `blocked_reason` permet aux chercheurs d’auditer les exclusions et de les réviser si les preuves s’améliorent.

### La solution à long terme est l’empreinte du micrologiciel

Le classement des OUI limite les dégâts, mais ne rend pas un préfixe fabricant partagé propre à un produit. Une piste plus solide est la structure ordonnée des éléments d’information des requêtes de sondage 802.11. Les travaux en amont documentent cette signature TLV :

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Cette séquence décrit le comportement d’une pile de micrologiciel particulière, et non le propriétaire d’un bloc MAC. L’empreinte des requêtes de sondage est une technique établie d’identification des appareils. [Des travaux publiés sur l’empreinte de la couche MAC 802.11](https://doi.org/10.1155/2017/6235484) montrent que les éléments d’information des requêtes peuvent rester identifiants lorsque les adresses MAC tournent. Ils traitent aussi le problème décrit dans [l’issue #43 de flock-you](https://github.com/colonelpanichacks/flock-you/issues/43) : `Flock Camera net.` apparaît sur des adresses MAC locales successives en 2,4 et 5 GHz.

La signature nécessite une validation de terrain indépendante sur plusieurs matériels et versions de micrologiciel. Les captures malformées exigent aussi une analyse défensive. C’est néanmoins la bonne direction. La randomisation MAC condamne la correspondance OUI seule à l’échec.

______

## Pourquoi cela dépasse un seul dépôt

Les gens utilisent des cartes de surveillance pour décider où conduire, se garer, signaler, enquêter et s’organiser. Un faux repère détourne l’attention. Des dizaines de milliers peuvent discréditer les observations exactes qui les entourent.

La crédibilité est aussi asymétrique. Un fournisseur ou un critique n’a besoin que d’un repère ClickShare démontré faux pour contester tout le jeu de données. Nous en avons fourni 50 278. Les journalistes et associations peuvent reprendre un titre clair plus vite qu’une correction ultérieure ne peut le suivre.

La transparence open source gagne la confiance grâce à des méthodes vérifiables et à une incertitude visible. La publication des données brutes a révélé notre erreur, mais elle ne justifiait pas une interface qui exagérait la conclusion. Le correctif doit figurer là où le lecteur rencontre l’affirmation : champ, filtre, repère, légende et titre.

### Un appel à tous les projets de cartographie Flock et ALPR

Les autres projets de cartographie Flock et ALPR devraient également auditer leurs données. C’est une invitation à comparer les méthodes, pas une accusation selon laquelle toutes les cartes ont hérité de notre erreur.

[WiGLE](https://www.wigle.net/stats/) est le plus vaste jeu public d’observations WiFi consultable mondialement que nous connaissions. Cette portée rendait Flock Finder attrayant : une API pouvait transformer une liste de signatures étudiées sur le terrain en carte mondiale. Elle rendait aussi l’erreur assez grande pour la mesurer. Une base mondiale renvoie tous les produits sans rapport qui partagent l’espace d’adresses d’un fournisseur radio, pas seulement le produit visé par la recherche.

Les autres cartes s’appuient sur des preuves différentes. Certaines utilisent des photos et des observations de terrain bénévoles . D’autres importent les balises de surveillance OpenStreetMap, des dossiers publics, des déclarations de fournisseurs ou les données d’un autre projet communautaire. Leurs totaux ne se comparent pas directement à nos résultats WiGLE, et notre taux de 2,4 % confirmé par SSID ne doit pas être extrapolé à un jeu vérifié sur le terrain. Le risque commun est qu’une classification passe d’un projet aux données sources d’un autre, puis paraisse être une corroboration indépendante.

Chaque carte publique devrait pouvoir répondre à un audit bref :

1. **Que signifie un repère ?** Un appareil photographié, un dossier public, une correspondance OUI, un signalement utilisateur ou une importation d’une autre carte ?
2. **Combien d’enregistrements disposent d’une preuve directe sur le produit ?** Publiez les comptes par classe de preuve au lieu d’un total unique.
3. **Quelles sources sont indépendantes ?** Suivez la provenance des importations afin que la même observation ne compte pas comme plusieurs confirmations.
4. **Qu’est-ce qui contredit la classification ?** Calculez les fréquences de SSID, fournisseurs, pays, étiquettes de contributeurs et autres champs catégoriels.
5. **Comment l’incertitude et les contestations sont-elles affichées ?** Montrez la confiance et l’état des corrections dans les repères, filtres, exports et titres.
6. **Un autre chercheur peut-il reproduire le compte ?** Publiez la requête, l’instantané source, les règles de classification et la date.

Cet audit ne réduit pas le problème Flock. Un réseau de caméras ALPR peut toujours enregistrer les déplacements, permettre des recherches entre juridictions et toucher des personnes qui n’ont jamais consenti à la collecte. Des comptes exacts rendent cette critique plus difficile à écarter. Si nous contestons les systèmes de surveillance, nos cartes doivent distinguer ce qui a été observé, déduit et confirmé.

Nous avons commis une erreur bien informée. Les préfixes venaient de recherches de terrain légitimes, le pipeline était reproductible et les réserves étaient réelles. L’inférence dépassait tout de même les preuves. De bonnes intentions et de bonnes données d’entrée n’annulent pas l’obligation de tester les résultats d’un système à grande échelle.

______

## Reproduire l’audit

Récupérez le commit `5551829`, puis exécutez ce qui suit à la racine du dépôt. Le script utilise uniquement la bibliothèque standard Python et affiche le total, la géographie, les SSID courants et quelques familles d’appareils nommés.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("lignes", len(rows))
print("États-Unis", countries["US"])
print("hors des États-Unis", sum(countries.values()) - countries["US"] - countries[""])
print("pays manquant", countries[""])
print("SSID les plus fréquents", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Pour les données historiques exactes, utilisez le CSV de ce commit, pas un jeu généré actuel. Le projet a cessé de versionner le grand CSV, le GeoJSON et les fichiers par OUI après l’audit, car chaque analyse réécrivait des centaines de mégaoctets et faisait grossir le dépôt. Les données générées actuelles sont restaurées depuis la version roulante [`data-latest`](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest) et publiées là. Le petit résumé `scan_stats.json` reste dans Git. L’absence d’un fichier généré dans la branche actuelle ne signifie donc ni que les preuves historiques ont disparu ni que leur compte est nul.

______

## La leçon

**Une heuristique marquée « suspectée » dans les métadonnées, mais affichée comme un repère certain sur la carte, est une affirmation.** L’étiquette doit figurer dans le modèle de données et la visualisation, pas seulement dans la documentation.

