---
title: "Compatibilité des alimentations de l’Octominer X12 Ultra : essai terrain Chicony et LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Un essai avec cinq ventilateurs et trois alimentations sur un Octominer X12 Ultra a montré qu’un bloc Chicony démarrait la machine, tandis que les LiteOn testés signalaient l’ambre et ne démarraient pas."
genre: ["Matériel de minage", "Matériel informatique"]
tags: ["Octominer X12 Ultra", "alimentation serveur", "compatibilité d’alimentation", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Illustration abstraite de trois alimentations serveur dans un châssis avec des voyants verts, ambre et gris"
coverCaption: ""
---

**La Chicony R12-1K6P2A a démarré mon Octominer X12 Ultra à cinq ventilateurs et trois alimentations.** Les blocs LiteOn PS-2142-2L testés ont affiché un voyant vert, puis sont passés à l’ambre sans démarrer la machine. Ce résultat concerne mon unité dotée d’une carte d’alimentation **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. Une puissance identique ou une liste destinée à une carte breakout X12 distincte ne prouve pas la compatibilité avec une carte Octominer.

Le châssis était vendu en **configuration de 3 600 W** avec trois emplacements d’alimentation. [Octominer indique une option avec trois blocs de 1 200 W](https://octominer.eu/product/octominer-x12-ultra-used/) pour le X12 Ultra, parmi d’autres configurations. Vérifiez l’étiquette et la carte d’alimentation de votre machine avant d’appliquer ces résultats.

## Résultats des essais

| Alimentation | Résultat sur cette machine |
|---|---|
| **Chicony R12-1K6P2A, 1 600 W** | A démarré la machine lors de mon essai. Cet article n’a pas mesuré la charge soutenue ni le fonctionnement dans tous les emplacements. |
| **LiteOn PS-2142-2L, 1 400 W** | Les blocs testés ont affiché le vert, puis l’ambre, et la machine n’a pas démarré. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | L’entrée secteur inhabituelle a compliqué la recherche d’un cordon adapté. Je n’ai enregistré aucun résultat de démarrage ou de charge pour cette alimentation. |
| **HP HSTNS-PD30, 1 200 W** | Testée dans la même machine. Le système n’a pas démarré. |
| **Autres blocs HP Common Slot** | Les kits Platinum Plus de 1 200 W et les modèles 750 W HSTNS-PD22B, HSTNS-PL22B et HSTNS-PD18 testés n’ont pas démarré cette machine. Les références exactes des blocs inclus dans les kits n’ont pas été notées. |

**N’interprétez pas le résultat LiteOn comme un diagnostic de panne pour tous les PS-2142-2L.** La séquence observée indique un échec de démarrage dans ce châssis. L’essai n’a isolé ni le signal d’activation, ni l’échange télémétrique, ni le brochage de la carte, ni un défaut d’un bloc donné. De même, le résultat Chicony établit un démarrage réussi, pas une puissance certifiée de 4 800 W pour le châssis ni une fiabilité à long terme.

## Quelle Chicony a démarré la machine ?

Le modèle qui a fonctionné était la **Chicony R12-1K6P2A**, également référencée **R1K6A002L** dans le [tableau de compatibilité de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Son [rapport d’essai 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifie un bloc de 1 600 W prévu pour **200 à 240 V CA**, 10 A et 50 à 60 Hz. Le rapport a mesuré un rendement de 94,19 % à mi-charge dans ses conditions d’essai à 230 V. Ces chiffres décrivent le bloc testé, pas l’ensemble de la machine de minage.

La plage de **200 à 240 V compte**. Ne supposez pas que ce modèle fournit sa puissance nominale sur une prise de 120 V. Selon une [fiche de pièces serveur pour ce modèle exact](https://www.itcreations.com/product/142080), le bloc testé possède une entrée C14 standard. Utilisez des cordons et du matériel de distribution adaptés à la tension et au courant d’entrée.

Mon essai a établi un démarrage réussi avec la Chicony sur cette carte précise. Il ne prouve pas la compatibilité avec toutes les révisions du X12 Ultra. Vérifiez la référence complète et l’étiquette de l’alimentation avant d’en commander d’autres.

## Pourquoi la liste LiteOn m’a induit en erreur

La **LiteOn PS-2142-2L** figure dans le [tableau de compatibilité des cartes breakout X12 de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Son [rapport 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifie un modèle de 1 400 W. Ces sources confirment le modèle et son usage répertorié avec **l’adaptateur X12 de Parallel Miner**. Aucune ne teste la carte d’alimentation OEM Octominer.

Mes blocs PS-2142-2L sont passés du **vert à l’ambre** après insertion, et la machine n’a pas démarré. Des lames de sortie de forme similaire ne prouvent pas un comportement identique au démarrage, pour l’état ou les communications. La séquence des voyants ne prouve pas à elle seule quelle différence a causé l’échec.

Le même [tableau Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) regroupe les **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** et **Chicony R12-1K6P2A** dans une famille d’adaptateurs à huit broches. Il place le **HP HSTNS-PD30** et plusieurs alimentations HP Common Slot de 750 W dans une autre famille à six broches. Aucun des blocs HP testés n’a démarré cette machine. Le tableau décrit les cartes Parallel Miner, pas une liste de remplacement pour la carte **OCTOMINER (12PIN)**.

## Vérifier l’alimentation et le câblage

Le [guide de dépannage de l’Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) indique que le châssis seul consomme jusqu’à **200 W** lorsque les ventilateurs tournent à pleine vitesse. Il recommande une réserve de puissance d’au moins **10 %** et déconseille de dépasser **90 % de la puissance nominale des blocs installés**. Tenez compte des GPU, du châssis et de la puissance réellement fournie par les alimentations à votre tension secteur.

**L’étiquette de 1 600 W sur chaque Chicony ne fait pas passer la configuration publiée du châssis de 3 600 W à 4 800 W.** La carte d’alimentation, le câblage interne, les connecteurs, la distribution secteur et le refroidissement limitent aussi le système. Je n’ai pas mesuré ces limites sur cette unité. Gardez la machine dans sa configuration documentée jusqu’à ce qu’Octominer confirme une puissance supérieure pour la révision exacte de la carte.

Le Dell/Delta **D1200E-S0 / 0F37X3** posait un autre problème : son entrée secteur côté alimentation exigeait un cordon correspondant moins courant. Lors d’une recherche précédente, j’ai identifié l’entrée comme **LS-25** et le connecteur côté cordon comme **LS-26**, d’après le bloc et les fiches de câbles. Vérifiez la forme du connecteur et les indications électriques avant d’acheter un cordon. Une prise C13 d’apparence familière ne remplace pas le connecteur correspondant.

## Vérifier votre X12

1. **Relevez le matériel exact.** Photographiez l’étiquette du châssis, celle de l’alimentation, l’entrée secteur, la lame de sortie et la révision de la carte d’alimentation. Comptez les ventilateurs et les emplacements.
2. **Vérifiez l’alimentation secteur.** Comparez la tension d’entrée du bloc aux caractéristiques de la prise, du cordon et de la PDU. Le rapport Chicony R12-1K6P2A indique 200 à 240 V CA.
3. **Testez une configuration minimale.** Arrêtez la machine et débranchez toutes les alimentations secteur avant de changer un bloc, un GPU ou une connexion PSON. [Le guide d’Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recommande de vérifier le bon enclenchement et les voyants du bloc, le câble PSON à six broches entre la carte mère et la carte d’alimentation, puis un bloc avec un GPU pour isoler un problème de démarrage.
4. **Consignez le résultat.** Notez le modèle, l’emplacement, la séquence des voyants, le démarrage de la carte et des ventilateurs, ainsi que celui de la machine. Ne répétez le test sur d’autres emplacements qu’après un arrêt sûr.
5. **Mesurez avant d’ajouter de la charge.** Vérifiez la télémétrie de l’alimentation et la consommation à la prise sous la charge GPU prévue. Le démarrage observé dans cet article ne remplace pas un essai en charge.

## Conclusion

**La Chicony R12-1K6P2A est la seule alimentation de cette comparaison dont le démarrage réussi est rapporté dans mon X12 Ultra à trois emplacements.** Les LiteOn PS-2142-2L testées sont passées du vert à l’ambre sans démarrer. Les HP Common Slot testées n’ont pas démarré la machine non plus. Considérez les autres listes d’alimentations comme des pistes de recherche jusqu’à ce que le modèle exact et la carte Octominer réussissent un démarrage et un essai en charge contrôlés. Commencez par les références et la révision de la carte, puis suivez les recommandations d’alimentation d’Octominer avant d’augmenter la charge GPU.
