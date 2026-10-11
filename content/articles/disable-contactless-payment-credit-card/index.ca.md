---
title: "Com desactivar el pagament sense contacte d'una targeta de crèdit"
date: 2026-10-02
lastmod: 2026-10-10
toc: true
draft: false
description: "Guia pràctica per desactivar el pagament sense contacte d'una targeta de crèdit de reserva mentre mantens disponibles els pagaments amb xip i banda magnètica, amb límits de seguretat i millors alternatives."
genre: ["Seguretat dels pagaments", "Privacitat digital", "NFC", "Seguretat personal", "Tecnologia de consum"]
tags: ["desactivar el pagament sense contacte", "desactivar NFC de la targeta de crèdit", "antena NFC de la targeta de crèdit", "pagament sense contacte", "pagar amb un toc", "conflicte de targetes", "Google Pay", "Apple Pay", "seguretat de la targeta de crèdit", "banda magnètica", "xip EMV", "antena NFC", "privacitat de la targeta de pagament"]
cover: "/img/cover/A_person_holding_a_credit_card_in_one_hand_and_a_lock.webp"
coverAlt: "Una persona sosté una targeta de crèdit al costat d'un símbol de cadenat, que representa el control sobre les funcions de la targeta de pagament."
coverCaption: "Desactiva el pagament sense contacte d'una targeta de reserva sense substituir els altres mètodes de pagament."
---

**Una targeta sense contacte té una antena NFC separada.** Si guardes la targeta dins de la funda del telèfon, l'antena pot provocar conflictes entre targetes o alertes NFC repetides en alguns telèfons. Una interrupció física del circuit de l'antena desactiva el pagament amb un toc, mentre el xip i la banda magnètica continuen disponibles en algunes targetes.

*Utilitza una targeta de reserva per a aquest projecte. Considera la modificació permanent i confirma el resultat amb l'emissor de la targeta abans de confiar-hi.*

**No modifiquis el teu únic mètode de pagament.** Les normes de l'emissor, la construcció de la targeta i el suport dels terminals varien. Tingues una segona targeta o efectiu disponible mentre proves la targeta danyada.

## Per què desactivar el pagament sense contacte?

Pagar amb un toc és còmode, i les carteres mòbils modernes afegeixen un altre testimoni de pagament al mateix telèfon. El problema comença quan una targeta física amb NFC queda a prop del lector NFC del telèfon.

Dos instruments de pagament poden respondre al mateix lector. Android també pot detectar la targeta física quan obres o agafes el telèfon. Treure la targeta de la funda resol el problema, però afegeix fricció cada vegada que pagues.

L'objectiu és concret: desactivar la interfície sense contacte de la targeta i mantenir disponibles els altres mètodes de pagament.

| Mètode de pagament | Resultat esperat després de trencar l'antena |
|---|---|
| **Pagament sense contacte** | Desactivat perquè el circuit de l'antena NFC ja no s'acobla al lector |
| **Xip EMV** | Sovint continua disponible si el xip i els seus contactes no es toquen |
| **Banda magnètica** | Sovint continua disponible si no es toca la banda |
| **Pagaments amb targeta en línia** | Normalment no es veuen afectats, però l'emissor pot substituir o desactivar la targeta després del dany |

## Com funciona la targeta?

**L'antena NFC és un circuit conductor prim dins del plàstic.** Normalment recorre bona part del perímetre de la targeta. Un lector sense contacte alimenta la targeta mitjançant aquest circuit i intercanvia dades amb el xip NFC integrat.

El xip de contacte EMV utilitza contactes metàl·lics exposats a la cara de la targeta. La banda magnètica utilitza una banda separada a la part posterior. Aquests sistemes comparteixen el mateix cos de la targeta, però no necessiten el mateix circuit d'antena.

Aquesta separació explica la modificació. Trencar el circuit atura la comunicació NFC. No esborra el número de la targeta, no destrueix la banda ni elimina els contactes EMV quan el tall queda lluny d'aquests components.

## Les opcions de menor risc

La modificació física és l'últim recurs. Comprova primer aquestes opcions:

- **Demana a l'emissor una substitució sense contacte.** Alguns emissors ofereixen variants de targeta sense pagament amb un toc.
- **Guarda la targeta lluny del telèfon.** Una funda separada elimina la col·lisió NFC sense canviar la targeta.
- **Utilitza un porta-targetes amb protecció.** Prova'l amb el telèfon i la targeta abans de confiar-hi per pagar.
- **Utilitza un testimoni de cartera virtual.** Apple Pay i Google Pay permeten que el telèfon gestioni el pagament sense contacte mentre la targeta física queda de reserva.
- **Utilitza una targeta de reserva diferent.** Mantenir la targeta modificada fora de l'ús diari evita una fallada al comerç.

*No posis la targeta al microones, no la cremis, no la dobleguis ni la perforis a prop del xip. Aquests mètodes causen danys innecessaris i et poden exposar a calor, fragments afilats o una fallada del mètode de pagament de reserva.*

## Modificació de l'antena

El mètode descrit pels exemples enllaçats és senzill en concepte: localitza el circuit de l'antena i fes-hi una petita interrupció amb una eina fina. El recorregut exacte de l'antena varia segons el disseny de la targeta, així que no copiïs una ubicació d'una targeta a una altra.

Una llanterna potent darrere de la targeta pot revelar el recorregut de l'antena. Algunes targetes mostren un fil o circuit visible a prop del perímetre. Mantén la interrupció lluny del xip EMV, dels seus contactes, de la banda magnètica, dels números en relleu i de les marques visibles de l'emissor.

Treballa sobre una superfície estable amb protecció ocular. Subjecta la targeta abans de tallar o perforar. Aplica una pressió controlada, atura't quan el circuit es trenqui i revisa les dues cares per detectar esquerdes. Un tall o forat petit és suficient. Més dany no millora el resultat.

El resultat és permanent. Una targeta danyada queda fora d'algunes polítiques de substitució de l'emissor, i un terminal pot rebutjar targetes amb el cos esquerdat o els contactes desalineats. Tingues un altre mètode de pagament disponible abans de provar-la.

## Prova el resultat

Prova cada funció per separat:

1. Allunya la targeta del telèfon i prova-la en un lector sense contacte. El pagament amb un toc hauria de fallar si el circuit de l'antena està trencat.
2. Insereix la targeta en un terminal compatible i prova el xip EMV amb el PIN requerit.
3. Prova la banda magnètica només on el comerç i l'emissor encara l'admetin.
4. Consulta el compte de la targeta o truca a l'emissor per confirmar que la targeta continua activa.
5. Afegeix la targeta a la cartera del telèfon només si l'emissor admet el testimoni de cartera i encara vols pagaments sense contacte des del telèfon.

No facis la prova amb una compra important. Utilitza una transacció de poc valor i tingues una segona targeta o efectiu disponible.

## Demostració en vídeo

El vídeo següent mostra la modificació física i explica per què trencar el circuit de l'antena atura el funcionament sense contacte:

{{< youtube id="XH_st471JEU" enable="true" title="Per què la meva targeta de crèdit té un forat?" >}}

El vídeo és una demostració, no una garantia per a tots els dissenys de targeta. Utilitza'l per entendre el concepte i inspecciona la teva targeta abans de decidir si el risc és acceptable.

## Què mostren les fonts?

Els exemples següents utilitzen dos enfocaments relacionats. Art Chaidarun descriu fer un petit tall al circuit de l'antena mentre manté funcionals el xip i la banda. La guia d'Instructables documenta un enfocament físic semblant per desactivar el pagament sense contacte d'una targeta de dèbit. El debat del fòrum afegeix un avís útil: trenca el circuit lluny del xip EMV en lloc de perforar al seu costat.

Aquests informes descriuen targetes individuals. No estableixen una disposició universal de l'antena ni prometen l'aprovació de l'emissor després de la modificació. Les normes de substitució i desactivació de l'emissor de la teva targeta determinen el resultat final.

## Referències

1. [Art Chaidarun, Com desactivar el pagament sense contacte d'una targeta de crèdit](https://chaidarun.com/disable-contactless-payment)
2. [Instructables, Com desactivar el pagament sense contacte de la teva targeta de dèbit](https://www.instructables.com/How-to-Disable-Contactless-Payment-on-Your-Debit-C/)
3. [Dangerous Things Forum, La manera més fàcil de desactivar NFC en una targeta de crèdit](https://forum.dangerousthings.com/t/easiest-way-of-disabling-nfc-in-a-credit-card/)
4. [DeviantOllam, Per què la meva targeta de crèdit té un forat?](https://www.youtube.com/watch?v=XH_st471JEU)

## Passos següents

Si necessites una targeta de pagament per a una funda de telèfon, comença amb una targeta sense contacte aprovada per l'emissor o amb una funda separada. Si modifiques una targeta de reserva, prova tots els mètodes de pagament restants abans de portar-la com a única reserva.

Per obtenir detalls relacionats amb les targetes de pagament, llegeix la [guia de targetes virtuals de Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/) i utilitza el [descodificador de banda magnètica](/magnetic-stripe-decoder/) per estudiar les dades desades a les pistes 1 i 2.
