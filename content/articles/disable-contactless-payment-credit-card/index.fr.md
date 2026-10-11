---
title: "Comment désactiver le paiement sans contact sur une carte de crédit"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "Guide pratique pour désactiver le paiement sans contact sur une carte de crédit de secours tout en gardant les paiements par puce et par bande magnétique disponibles, avec des limites de sécurité et de meilleures alternatives."
genre: ["Sécurité des paiements", "Confidentialité numérique", "NFC", "Sécurité personnelle", "Technologie grand public"]
tags: ["désactiver le paiement sans contact", "désactiver le NFC d'une carte de crédit", "antenne NFC de carte de crédit", "paiement sans contact", "paiement sans contact", "conflit de cartes", "Google Pay", "Apple Pay", "sécurité des cartes de crédit", "bande magnétique", "puce EMV", "antenne NFC", "confidentialité des cartes de paiement"]
cover: "/img/cover/A_person_holding_a_credit_card_in_one_hand_and_a_lock.webp"
coverAlt: "Une personne tient une carte de crédit à côté d'un symbole de cadenas, ce qui représente le contrôle des fonctions de la carte de paiement."
coverCaption: "Désactivez le paiement sans contact sur une carte de secours sans remplacer ses autres moyens de paiement."
---

**Une carte sans contact possède une antenne NFC distincte.** Si vous gardez la carte dans une coque de téléphone, l'antenne provoque un conflit de cartes ou des alertes NFC répétées sur certains téléphones. Une rupture physique de la boucle d'antenne désactive le paiement sans contact, tandis que la puce et la bande magnétique restent disponibles sur certaines cartes.

*Utilisez une carte de secours pour ce projet. Considérez la modification comme permanente et confirmez le résultat auprès de l'émetteur de la carte avant de vous y fier.*

**Ne modifiez pas votre seul moyen de paiement.** Les règles de l'émetteur, la construction de la carte et la prise en charge des terminaux diffèrent. Gardez une deuxième carte ou des espèces pendant le test de la carte endommagée.

## Pourquoi désactiver le paiement sans contact ?

Le paiement sans contact est pratique, et les portefeuilles mobiles modernes ajoutent un autre jeton de paiement au même téléphone. Le problème commence lorsqu'une carte physique compatible NFC se trouve près du lecteur NFC du téléphone.

Deux moyens de paiement pourraient répondre au même lecteur. Android pourrait aussi détecter la carte physique lorsque vous ouvrez ou manipulez le téléphone. Retirer la carte de la coque résout le problème, mais ajoute une contrainte à chaque paiement.

L'objectif est limité : désactiver l'interface sans contact de la carte tout en gardant les autres moyens de paiement disponibles.

| Moyen de paiement | Résultat attendu après une rupture de l'antenne |
|---|---|
| **Paiement sans contact** | Désactivé, car la boucle d'antenne NFC ne se couple plus avec un lecteur |
| **Puce EMV** | Souvent disponible si la puce et ses contacts restent intacts |
| **Bande magnétique** | Souvent disponible si la bande reste intacte |
| **Paiements par carte en ligne** | Généralement inchangés, mais l'émetteur pourrait remplacer ou désactiver la carte après les dommages |

## Fonctionnement de la carte

**L'antenne NFC est une fine boucle conductrice dans le plastique.** Elle suit généralement une grande partie du périmètre de la carte. Un lecteur sans contact alimente la carte par cette boucle et échange des données avec la puce NFC intégrée.

La puce de contact EMV utilise des contacts métalliques exposés sur la face de la carte. La bande magnétique utilise une bande distincte au dos. Ces systèmes partagent le même corps de carte, mais n'ont pas besoin de la même boucle d'antenne.

Cette séparation explique la modification. Rompre la boucle arrête la communication NFC. Cela n'efface pas le numéro de carte, ne détruit pas la bande et ne retire pas les contacts EMV si la coupure reste éloignée de ces composants.

## Options présentant moins de risques

La modification physique est un dernier recours. Vérifiez d'abord ces options :

- **Demandez à l'émetteur une carte de remplacement sans contact.** Certains émetteurs proposent des variantes sans paiement sans contact.
- **Rangez la carte loin du téléphone.** Un étui séparé supprime le conflit NFC sans modifier la carte.
- **Utilisez un porte-cartes blindé.** Testez le porte-cartes avec le téléphone et la carte avant de vous y fier pour payer.
- **Utilisez un jeton de portefeuille virtuel.** Apple Pay et Google Pay permettent au téléphone de gérer le paiement sans contact tandis que la carte physique reste en réserve.
- **Utilisez une autre carte de secours.** Garder la carte modifiée hors de l'usage quotidien évite une défaillance chez un commerçant.

*Ne mettez pas la carte au micro-ondes, ne la brûlez pas, ne la pliez pas et ne la percez pas près de la puce. Ces méthodes causent des dommages inutiles et pourraient vous exposer à la chaleur, à des fragments tranchants ou à l'échec de votre moyen de paiement de secours.*

## Modification de l'antenne

La méthode décrite dans les exemples liés est simple en principe : repérez la boucle d'antenne, puis créez une petite rupture dans la boucle avec un outil fin. Le trajet exact de l'antenne varie selon le modèle de carte. Ne reproduisez donc pas un emplacement d'une carte sur une autre.

Une lampe de poche puissante placée derrière la carte pourrait révéler le trajet de l'antenne. Certaines cartes montrent un fil ou une boucle visible près du bord. Éloignez la rupture de la puce EMV, de ses contacts, de la bande magnétique, des chiffres en relief et de tout marquage visible de l'émetteur.

Travaillez sur une surface stable et portez des lunettes de protection. Fixez la carte avant de la couper ou de la percer. Exercez une pression contrôlée, arrêtez-vous lorsque la boucle est rompue et inspectez les deux faces pour repérer les fissures. Une petite coupure ou un petit trou suffit. Des dommages supplémentaires n'améliorent pas le résultat.

Le résultat est permanent. Une carte endommagée sort du cadre de certaines politiques de remplacement de l'émetteur, et un terminal de commerçant refuse les cartes dont le corps est fissuré ou dont les contacts sont mal alignés. Gardez un autre moyen de paiement disponible avant de la tester.

## Tester le résultat

Testez chaque fonction séparément :

1. Éloignez la carte du téléphone et essayez-la sur un lecteur sans contact. Le paiement sans contact devrait échouer si la boucle d'antenne est rompue.
2. Insérez la carte dans un terminal compatible et testez la puce EMV avec le PIN requis.
3. Testez la bande magnétique uniquement là où le commerçant et l'émetteur la prennent encore en charge.
4. Vérifiez le compte de la carte ou appelez l'émetteur pour confirmer que la carte reste active.
5. Ajoutez la carte au portefeuille du téléphone uniquement si l'émetteur prend en charge le jeton du portefeuille et si vous souhaitez encore effectuer des paiements sans contact avec le téléphone.

Ne faites pas le test avec un achat important. Utilisez une transaction de faible montant et gardez une deuxième carte ou des espèces disponibles.

## Démonstration vidéo

La vidéo suivante montre la modification physique et explique pourquoi la rupture de la boucle d'antenne arrête le fonctionnement sans contact :

{{< youtube id="XH_st471JEU" enable="true" title="Pourquoi ma carte de crédit a-t-elle un trou ?" >}}

La vidéo est une démonstration, pas une garantie pour chaque modèle de carte. Utilisez-la pour comprendre le principe, puis inspectez votre propre carte avant de décider si le risque vous convient.

## Ce que montrent les sources

Les exemples ci-dessous présentent deux approches proches. Art Chaidarun décrit une petite coupure dans la boucle d'antenne tout en gardant la puce et la bande fonctionnelles. Le guide Instructables décrit une approche physique similaire pour désactiver le paiement sans contact sur une carte de débit. La discussion du forum ajoute un avertissement utile : rompez la boucle loin de la puce EMV au lieu de percer à côté.

Ces témoignages décrivent des cartes individuelles. Ils n'établissent pas un emplacement universel de l'antenne et ne promettent pas l'accord de l'émetteur après la modification. Les règles de remplacement et de désactivation de votre émetteur déterminent le résultat final.

## Références

1. [Art Chaidarun, Comment désactiver le paiement sans contact sur une carte de crédit](https://chaidarun.com/disable-contactless-payment)
2. [Instructables, Comment désactiver le paiement sans contact sur votre carte de débit](https://www.instructables.com/How-to-Disable-Contactless-Payment-on-Your-Debit-C/)
3. [Forum Dangerous Things, Méthode la plus simple pour désactiver le NFC d'une carte de crédit](https://forum.dangerousthings.com/t/easiest-way-of-disabling-nfc-in-a-credit-card/)
4. [DeviantOllam, Pourquoi ma carte de crédit a-t-elle un trou ?](https://www.youtube.com/watch?v=XH_st471JEU)

## Prochaines étapes

Si vous avez besoin d'une carte de paiement dans une coque de téléphone, commencez par une carte sans contact approuvée par l'émetteur ou par un étui séparé. Si vous modifiez une carte de secours, testez tous les moyens de paiement restants avant de la transporter comme seule carte de secours.

Pour des informations connexes sur les cartes de paiement, lisez le [guide des cartes virtuelles Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/) et utilisez le [décodeur de bande magnétique](/magnetic-stripe-decoder/) pour étudier les données stockées sur les pistes 1 et 2.
