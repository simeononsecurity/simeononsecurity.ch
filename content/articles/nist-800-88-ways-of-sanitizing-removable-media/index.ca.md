---
title: "Mètodes aprovats pel NIST per sanejar suports extraïbles"
date: 2023-02-11
lastmod: 2026-11-11
toc: true
draft: false
description: "Coneix els mètodes del NIST per sanejar discs durs, SSD, unitats USB i discs òptics i protegir les dades sensibles d'accessos no autoritzats."
tags: ["Mètodes aprovats pel NIST", "Sanejament de suports extraïbles", "Discs durs", "SSD", "Unitats flash USB", "CD", "DVD", "Discs Blu-ray", "Seguretat de les dades", "Protecció de dades sensibles"]
cover: "/img/cover/An_image_of_a_person_holding_a_USB_flash_drive_with_a_shreder.webp"
coverAlt: "Una persona sosté una unitat USB amb una trituradora al fons."
coverCaption: ""
---

Els suports extraïbles, com ara discs durs, unitats d'estat sòlid (SSD), unitats flash USB, CD, DVD i discs Blu-ray, són part essencial del món digital actual. S'utilitzen àmpliament per emmagatzemar i transferir dades sensibles. Per això, cal impedir que la informació que contenen es filtri o quedi a l'abast de persones no autoritzades. Aquest article explica els mètodes aprovats pel NIST per sanejar tota mena de suports extraïbles.

## Per què cal sanejar els suports extraïbles?

**Sanejar els suports extraïbles és essencial perquè les dades que contenen es poden recuperar fàcilment, fins i tot després d'esborrar-les.** Quan s'esborren dades, només se n'elimina la referència. Les dades reals continuen al disc fins que se sobreescriuen. Això permet que actors maliciosos recuperin informació sensible amb programari de recuperació de dades.

## Tipus de destrucció de NIST 800-88 Revision 1

El National Institute of Standards and Technology (NIST) ha publicat unes directrius per al sanejament de suports extraïbles, conegudes com a NIST Special Publication 800-88 Revision 1. Hi descriu diversos mètodes, com ara la destrucció física, el clear i el purge.

### Destrucció física

**La destrucció física és el mètode més segur per sanejar suports extraïbles.** Consisteix a destruir físicament el dispositiu perquè ningú no en pugui recuperar les dades. Es pot triturar, fondre o polvoritzar.

### Clear

El clear és el procés de sobreescriure les dades d'un dispositiu amb una sèrie de valors binaris. És menys segur que la destrucció física, però continua sent eficaç per sanejar la majoria de suports extraïbles. NIST 800-88 Revision 1 recomana fer servir una eina de programari que compleixi els estàndards establerts pel Departament de Defensa dels Estats Units (DoD), especificació [5220.22-M](https://simeononsecurity.com/articles/dod-5220.22-m-data-sanitization-summarized/).

### Purge

El purge és el procés de sobreescriure diverses vegades les dades d'un dispositiu amb un patró de valors binaris. És més segur que el clear i es recomana per a dades sensibles. NIST 800-88 Revision 1 recomana fer servir una eina de programari que compleixi l'estàndard [DoD 5220.22-M](https://simeononsecurity.com/articles/dod-5220.22-m-data-sanitization-summarized/).

__________________________________________

## Conclusió

En resum, **sanejar els suports extraïbles és essencial per impedir que les dades sensibles que contenen es filtrin o quedin a l'abast de persones no autoritzades.** NIST 800-88 Revision 1 ofereix directrius per sanejar tots els tipus de suports extraïbles, com ara discs durs, SSD, unitats flash USB, CD, DVD i discs Blu-ray, mitjançant destrucció física, clear i purge. **La destrucció física és el mètode més segur, però el clear i el purge també són eficaços i ofereixen un nivell de seguretat alt.**

**El sanejament dels suports extraïbles és només una part d'una estratègia completa de seguretat de les dades.** També cal aplicar mesures com el xifratge i l'emmagatzematge segur per protegir les dades sensibles.
