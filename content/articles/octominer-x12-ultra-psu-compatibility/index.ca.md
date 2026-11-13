---
title: "Compatibilitat de fonts de l’Octominer X12 Ultra: prova de camp de Chicony i LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Una prova amb cinc ventiladors i tres fonts en un Octominer X12 Ultra va mostrar que una font Chicony iniciava l’equip, mentre que les LiteOn provades mostraven llum ambre i no s’iniciaven."
genre: ["Maquinari de mineria", "Maquinari informàtic"]
tags: ["Octominer X12 Ultra", "font d’alimentació de servidor", "compatibilitat de fonts", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Il·lustració abstracta de tres fonts de servidor dins d’un xassís amb llums d’estat verdes, ambre i grises"
coverCaption: ""
---

**La Chicony R12-1K6P2A va iniciar el meu Octominer X12 Ultra de cinc ventiladors i tres fonts.** Les fonts LiteOn PS-2142-2L que vaig provar mostraven una llum verda, canviaven a ambre i no iniciaven l’equip. Aquest resultat correspon a la meva unitat amb una placa d’alimentació **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. La mateixa potència nominal o una llista per a una placa breakout X12 independent no demostren la compatibilitat amb una placa Octominer.

El xassís es venia com una **configuració de 3.600 W** amb tres espais per a fonts. [Octominer indica una opció de tres fonts de 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) per a l’X12 Ultra, entre altres configuracions. Revisa l’etiqueta i la placa d’alimentació del teu equip abans d’aplicar aquests resultats.

## Resultats de la prova

| Font | Resultat en aquest equip |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Va iniciar l’equip durant la meva prova. L’article no va mesurar càrrega sostinguda ni funcionament en tots els espais. |
| **LiteOn PS-2142-2L, 1.400 W** | Les unitats provades van mostrar verd i després ambre. L’equip no es va iniciar. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | L’entrada de CA poc habitual va dificultar trobar un cable adequat. No vaig registrar resultats d’arrencada ni de càrrega per a aquesta font. |
| **HP HSTNS-PD30, 1.200 W** | Provada en el mateix equip. No va iniciar el sistema. |
| **Altres unitats HP Common Slot** | Els kits Platinum Plus de 1.200 W i les unitats de 750 W HSTNS-PD22B, HSTNS-PL22B i HSTNS-PD18 que vaig provar no van iniciar aquest equip. No es van registrar els números de model exactes de les fonts dels kits. |

**No interpretis el resultat de LiteOn com un diagnòstic d’avaria de totes les PS-2142-2L.** La seqüència observada indica una fallada d’arrencada en aquest xassís. La prova no va aïllar el senyal d’activació, l’intercanvi de telemetria, el pinout de la placa ni una avaria d’una font individual. Igualment, el resultat de Chicony confirma un inici correcte, no una potència certificada del xassís de 4.800 W ni una fiabilitat a llarg termini.

## Quina Chicony va iniciar l’equip?

El model que va funcionar era **Chicony R12-1K6P2A**, també indicat com a peça **R1K6A002L** a la [taula de compatibilitat de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). El seu [informe de prova 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifica una font de 1.600 W amb una classificació de **200 a 240 V CA**, 10 A i 50 a 60 Hz. L’informe va mesurar un rendiment del 94,19% a mitja càrrega en les condicions de prova a 230 V. Aquestes xifres descriuen la font provada, no tot l’equip de mineria.

La classificació de **200 a 240 V és important**. No pressuposis que aquest model ofereix la potència nominal des d’una presa de 120 V. Segons una [fitxa de recanvis de servidor del model exacte](https://www.itcreations.com/product/142080), la font provada té una entrada C14 estàndard. Fes servir cables i equips de distribució adequats per a la tensió i el corrent d’entrada.

La meva prova va confirmar un inici correcte amb la Chicony en aquesta placa concreta. No demostra la compatibilitat amb totes les revisions de l’X12 Ultra. Comprova el número de model complet i l’etiqueta abans de demanar més unitats.

## Per què em va confondre la llista de LiteOn

La **LiteOn PS-2142-2L** apareix a la [taula de compatibilitat de plaques breakout X12 de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). El seu [informe 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifica un model de 1.400 W. Aquestes fonts confirmen el model i l’ús indicat amb **l’adaptador X12 de Parallel Miner**. Cap de les dues prova la placa d’alimentació OEM d’Octominer.

Les meves unitats PS-2142-2L van passar de **verd a ambre** després d’inserir-les, i l’equip no es va iniciar. Que les pales de sortida tinguin una forma semblant no demostra el mateix comportament d’inici, estat o comunicació. La seqüència dels LED, per si sola, no prova quina diferència va causar la fallada.

La mateixa [taula de Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) agrupa **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** i **Chicony R12-1K6P2A** dins de la família d’adaptadors de vuit pins. Situa **HP HSTNS-PD30** i diverses fonts HP Common Slot de 750 W dins d’una altra família d’adaptadors de sis pins. Cap unitat HP que vaig provar no va iniciar aquest equip. La taula descriu les plaques de Parallel Miner, no una llista de recanvis per a la placa **OCTOMINER (12PIN)**.

## Comprova l’alimentació i els cables

La [guia de resolució de problemes de l’Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) diu que el xassís sol consumeix fins a **200 W amb els ventiladors a màxima velocitat**. Recomana almenys un **10% de marge de potència** i adverteix que no s’ha de superar el **90% de la potència nominal de les fonts instal·lades**. Compta la potència de les GPU, el xassís i la sortida real de les fonts amb la teva tensió de CA.

**Una etiqueta de 1.600 W a cada font Chicony no converteix la configuració publicada de 3.600 W del xassís en una de 4.800 W.** La placa d’alimentació, els cables interns, els connectors, la distribució de CA i la refrigeració també limiten el sistema. No he mesurat aquests límits en aquesta unitat. Mantén l’equip dins de la configuració documentada fins que Octominer confirmi una potència superior per a la revisió exacta de la placa.

El Dell/Delta **D1200E-S0 / 0F37X3** presentava un altre problema: l’entrada de CA del costat de la font necessitava un cable d’acoblament menys habitual. En una cerca anterior vaig identificar l’entrada com a **LS-25** i el connector del cable com a **LS-26**, segons la unitat i els anuncis de cables. Verifica la forma del connector i les marques elèctriques abans de comprar un cable. Un endoll C13 d’aspecte familiar no substitueix el connector d’acoblament correcte.

## Verifica el teu X12

1. **Registra el maquinari exacte.** Fotografia l’etiqueta del xassís, la de la font, l’entrada de CA, la pala de sortida i la revisió de la placa d’alimentació. Compta els ventiladors i els espais per a fonts.
2. **Comprova l’alimentació de CA.** Compara la classificació d’entrada de la font amb les de la presa, el cable i la PDU. L’informe de la Chicony R12-1K6P2A especifica de 200 a 240 V CA.
3. **Prova una configuració mínima.** Apaga i desconnecta totes les entrades de CA abans de canviar una font, una GPU o una connexió PSON. [La guia d’Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recomana comprovar l’ajust i els LED de la font, el cable PSON de sis pins entre la placa base i la placa d’alimentació, i una font amb una GPU per aïllar un problema d’inici.
4. **Registra què ha passat.** Anota el model de la font, l’espai, la seqüència dels LED, si han iniciat la placa i els ventiladors, i si l’equip ha arrencat. Repeteix la prova en altres espais només després d’un tancament segur.
5. **Mesura abans d’afegir càrrega.** Comprova la telemetria de la font i el consum a la presa amb la càrrega prevista de les GPU. La prova d’inici d’aquest article no substitueix una prova de càrrega.

## Conclusió

**La Chicony R12-1K6P2A és l’únic recanvi d’aquesta comparació amb un inici correcte registrat al meu X12 Ultra de tres espais.** Les unitats LiteOn PS-2142-2L provades van passar de verd a ambre i no es van iniciar. Les unitats HP Common Slot provades tampoc van iniciar l’equip. Considera altres llistes de fonts com a pistes de recerca fins que el model exacte i la placa Octominer superin una prova controlada d’inici i càrrega. Comença per les etiquetes dels models i la revisió de la placa. Consulta les indicacions d’alimentació d’Octominer abans d’augmentar la càrrega de les GPU.
