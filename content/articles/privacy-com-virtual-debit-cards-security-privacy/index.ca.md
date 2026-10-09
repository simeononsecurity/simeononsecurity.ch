---
title: "Targetes Virtuals de Privacy.com: Com Funciona la Privacitat en el Pagament"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: Què s'emmagatzema en una targeta de pagament, per què la banda magnètica és la part més feble, què veu un comerciant quan pagues amb un número virtual, i com funcionen en la pràctica els tipus i límits de targetes de Privacy.com.
genre:
- Seguretat en el Pagament
- Privacitat Digital
- Targetes Virtuals
- Privacitat Financera
- Prevenció de Fraus
- Seguretat del Consumidor
tags:
- privacy.com
- targetes virtuals
- targetes de dèbit virtuals
- targetes d’un sol ús
- targetes bloquejades per comerciant
- targetes bloquejades per categoria
- tokenització
- token de xarxa
- pan
- cvv
- clonació de targetes
- banda magnètica
- pista 1
- pista 2
- seguretat de targetes de pagament
- fraus amb targetes de crèdit
- gestió de subscripcions
- límits de despesa
- pci dss
- soc 2
- fraus sense targeta física
- privacitat financera
- privacitat en el pagament
- número de targeta virtual
- targeta enmascarada
- controls de targeta
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Una il·lustració digital que mostra una targeta virtual protegida amb un escut que protegeix un símbol de cadenat, representant la seguretat i privacitat que ofereixen les targetes de dèbit virtuals.
coverCaption: Protegeix, Controla i Assegura les Teves Transaccions en Línia.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Una targeta virtual fa una cosa específica: canvia el que rep el comerciant, no el que sap el teu banc.** Aquest és tot el mecanisme, i entendre’l explica tant la protecció que obtens com la que no.

La majoria de cobertures tracten les targetes virtuals com una eina general de privacitat i eviten el detall tècnic. Aquest article explica què s’emmagatzema en una targeta, per què la banda magnètica és el punt feble, i com es comporten en la pràctica els tipus de targetes de Privacy.com.

*El benefici pràctic és concret i real: un número robat esdevé inútil per a un lladre, perquè només funciona amb el comerciant per al qual es va emetre.*

## La Resposta Breu

| Pregunta | Resposta Breu |
|---|---|
| **Què canvia una targeta virtual?** | El número que emmagatzema el comerciant. Les teves dades reals mai no arriben a ells |
| **La transacció és privada?** | No. El teu banc, la xarxa i l’emissor encara la veuen |
| **Què impedeix que una violació et perjudiqui?** | Un número bloquejat per comerciant o d’un sol ús, que falla en qualsevol altre lloc |
| **Quina és la part més feble d’una targeta física?** | La banda magnètica, que emmagatzema totes les dades de la pista sense xifrar |
| **Genera crèdit?** | No. No són comptes de crèdit i no es fa cap consulta de crèdit |
| **Qui pot usar Privacy.com?** | Ciutadans o residents legals dels EUA, majors de 18 anys, amb un compte corrent en un banc o cooperativa de crèdit dels EUA |

## Què Hi Ha en una Targeta de Pagament

**Tres coses autoritzen una transacció sense targeta física: el número principal de compte, la data de caducitat i el valor de verificació.**

| Element | Longitud | Origen |
|---|---|---|
| **Número Principal de Compte (PAN)** | Fins a 19 dígits | L’emissor, amb dígits inicials que identifiquen l’esquema i el banc |
| **Caducitat** | Quatre dígits en format MM/AA | L’emissor |
| **CVV o CVC** | Tres o quatre dígits | Derivat del PAN, caducitat i una clau que només té l’emissor |
| **Nom del titular** | Fins a 26 caràcters | Apareix només a la Pista 1 de la banda magnètica |

**El PAN no és una cadena aleatòria.** El primer dígit identifica l’esquema, els següents identifiquen el banc emissor, i la resta identifica el compte. Aquesta estructura permet comprovar la plausibilitat d’un número de targeta sense contactar ningú, i per això el dígit de control Luhn detecta un dígit transposat.

**El CVV és el que demostra que algú va tenir físicament la targeta** quan es va emetre. No s’emmagatzema a la banda magnètica, que és precisament per què un dispositiu que copia la banda mai no l’obté.

*Inspecciona tot això tu mateix amb el **[Decodificador i Codificador de Banda Magnètica](/magnetic-stripe-decoder/)**, que analitza la Pista 1 i la Pista 2, decodifica els dígits del codi de servei i torna a codificar el resultat. Funciona completament al navegador, cosa important perquè aquest és el contingut complet d’una targeta de pagament.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagrama que mostra els elements d’una targeta de pagament incloent el número principal de compte, data de caducitat, CVV, i les tres pistes de la banda magnètica amb què conté cadascuna" >}}

## Per què la Banda Magnètica és el Punt Feble

**La banda emmagatzema dades del compte en text pla, i qualsevol lector compatible les llegeix.**

Una banda magnètica conté fins a tres pistes. La Pista 1 porta el PAN, el nom del titular, la caducitat i un codi de servei de tres dígits, i és l’única pista que conté text alfabètic. La Pista 2 porta el PAN, la caducitat i el codi de servei en una codificació numèrica més densa, i **la Pista 2 és la que gairebé tots els terminals de punt de venda llegeixen.** La Pista 3 pràcticament no és usada per les grans xarxes i sovint no està present a la targeta.

El codi de servei és important d’entendre perquè descriu l’ús permès de la targeta. El primer dígit cobreix les regles d’intercanvi, el segon la gestió d’autoritzacions, i el tercer l’abast dels serveis. Una targeta codificada `201` permet intercanvi internacional, no necessita un camí d’autorització especial, i no té restriccions de servei.

La història explica per què la banda va durar tant. El 1969 un enginyer d’IBM anomenat Forrest Parry va intentar enganxar cinta magnètica a una targeta de plàstic i no va aconseguir que s’adherís sense danyar-la. La seva dona va suggerir usar una planxa de roba, i la calor va unir la cinta a la targeta. Aquesta improvisació es va convertir en l’estàndard durant més de mig segle.

Dos fets estan posant fi a això:

| Fita | Estat |
|---|---|
| **Mastercard va anunciar la retirada de la banda** | El 2033, cap targeta Mastercard de crèdit o dèbit en tindrà |
| **Europa** | Les bandes van començar a desaparèixer de les targetes Mastercard el 2024 |
| **Estats Units** | Els bancs deixaran d’emetre-les a partir del 2027 |

*La banda va ser substituïda per la xip i el pagament sense contacte perquè copiar-la no requereix cap habilitat més que tenir un lector. La nostra **[eina de banda magnètica](/magnetic-stripe-decoder/)** mostra quina poca dada cal per reconstruir una pista funcional.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagrama d’una banda magnètica que mostra la posició física de les pistes u, dos i tres, amb la disposició dels camps de cada pista incloent sentinelles, PAN, nom, caducitat i codi de servei" >}}

## Com Llegir les Dades de la Pista

**Una cadena de banda magnètica és una seqüència de camps, no un segon número de targeta.** El lector troba la sentinella d’inici, separa els camps, llegeix la caducitat i el codi de servei, després comprova la sentinella final i el LRC.

| Pista | Inici | Camps principals | Final | Conjunt de caràcters |
|---|---|---|---|---|
| **Pista 1** | `%` | Codi de format, PAN, nom, caducitat, codi de servei, dades discrecionals | `?` més LRC | ALPHA de sis bits, per tant conté lletres |
| **Pista 2** | `;` | PAN, caducitat, codi de servei, dades discrecionals | `?` més LRC | BCD de quatre bits, per tant conté dígits i un conjunt petit de puntuació |

Els sentinelles opcionals identifiquen els límits físics del registre. Un decodificador sovint els omet quan mostra els camps, però un codificador físic necessita el format complet del registre que espera el lector.

### Exemple de Pista 1

Aquest és un exemple sintètic. Utilitza el PAN de prova estàndard de l'eina i un nom fals, caducitat, codi de servei i dades discrecionals. No és una targeta de Privacy.com i no són dades de pagament vàlides.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Llegeix-ho d'esquerra a dreta:

| Segment | Valor | Significat |
|---|---|---|
| **Sentinella d'inici** | `%` | Comença el registre de la Pista 1 |
| **Codi de format** | `B` | Format de targeta financera B |
| **PAN** | `4111111111111111` | Número de compte primari sintètic |
| **Separador de camp** | `^` | Acaba el PAN i comença el nom |
| **Nom** | `TEST/USER` | Cognom, separador, nom de pila |
| **Separador de camp** | `^` | Acaba el nom i comencen els camps de transacció |
| **Caducitat** | `2912` | Desembre 2029 en format AA-MM |
| **Codi de servei** | `501` | Intercanvi nacional, processament normal, sense restriccions |
| **Dades discrecionals** | `0000000` | Omplidor definit per l'emissor en aquest exemple |
| **Sentinella de final** | `?` | Acaben les dades de la Pista 1 abans del LRC |

El registre codificat real també porta un caràcter LRC després de la sentinella de final quan el lector l'espera. La forma de text visible és útil per estudiar l'estructura. La representació a nivell de bit també porta paritat senar per a cada caràcter.

### Exemple de Pista 2

La Pista 2 elimina el nom i el codi de format. Els mateixos valors sintètics esdevenen:

```text
;4111111111111111=291250100000000?
```

| Segment | Valor | Significat |
|---|---|---|
| **Sentinella d'inici** | `;` | Comença el registre de la Pista 2 |
| **PAN** | `4111111111111111` | Número de compte primari sintètic |
| **Separador** | `=` | Acaba el PAN i comencen els camps de transacció |
| **Caducitat** | `2912` | Desembre 2029 en format AA-MM |
| **Codi de servei** | `501` | Mateix codi de servei sintètic que la Pista 1 |
| **Dades discrecionals** | `0000000` | Omplidor definit per l'emissor en aquest exemple |
| **Sentinella de final** | `?` | Acaben les dades de la Pista 2 abans del LRC |

**La Pista 2 és més curta perquè no té el nom del titular.** Molts terminals llegeixen la Pista 2 per a transaccions ordinàries amb passades, mentre que la Pista 1 proporciona el camp de nom quan un lector ho sol·licita.

### Dígits del Codi de Servei

**Els tres dígits del codi de servei descriuen el comportament del terminal i l'autorització.** No contenen el CVV, i canviar-los en una targeta real sense autorització de l'emissor produeix una credencial de pagament mal formada o enganyosa.

| Dígit | Valors | Què descriu |
|---|---|---|
| **Primer** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Regles d'intercanvi i preferència de xip |
| **Segon** | `0`, `1`, `2`, `4` | Ruta d'autorització |
| **Tercer** | `0` fins a `7` | Restriccions de PIN, efectiu, béns i serveis |

**El primer dígit** cobreix l'intercanvi i la preferència de xip:

| Valor | Significat |
|---|---|
| `0` | Ús nacional |
| `1` | Intercanvi internacional permès |
| `2` | Intercanvi internacional, ús de IC (xip) quan sigui possible |
| `5` | Només intercanvi nacional excepte sota acord bilateral |
| `6` | Només intercanvi nacional excepte sota acord bilateral, ús de IC quan sigui possible |
| `7` | Sense intercanvi excepte sota acord bilateral (circuit tancat) |
| `9` | Prova |

**El segon dígit** cobreix el maneig de l'autorització:

| Valor | Significat |
|---|---|
| `0` | Autorització normal |
| `1` | Autorització normal |
| `2` | Contactar l'emissor per mitjans en línia |
| `4` | Contactar l'emissor per mitjans en línia excepte sota acord bilateral |

**El tercer dígit** cobreix les restriccions de servei:

| Valor | Significat |
|---|---|
| `0` | Sense restriccions, es requereix PIN |
| `1` | Sense restriccions |
| `2` | Només béns i serveis (sense efectiu) |
| `3` | Només caixer automàtic, es requereix PIN |
| `4` | Només efectiu |
| `5` | Només béns i serveis (sense efectiu), es requereix PIN |
| `6` | Sense restriccions, usar PIN quan sigui possible |
| `7` | Només béns i serveis (sense efectiu), usar PIN quan sigui possible |

Per exemple, `201` significa intercanvi internacional amb ús de xip quan sigui possible, processament normal d'autorització i sense restriccions de servei. El decodificador mostra cada dígit per separat perquè no cal memoritzar la taula.

### LRC i Paritat

**El LRC és un caràcter de comprovació, no un altre camp a inventar.** El codificador fa XOR del valor de dades de cada caràcter des de la sentinella d'inici fins a la sentinella de final. Converteix el resultat de nou al rang de caràcters imprimibles de la pista i informa dels bits de paritat senar codificats per separat.

La Pista 1 utilitza un conjunt de caràcters ALPHA de sis bits. El seu valor de dades és el codi ASCII menys `0x20`. La Pista 2 utilitza un conjunt de caràcters BCD de quatre bits. El seu valor de dades és el nibble baix del codi ASCII. Aplicar la correspondència de la Pista 1 a la Pista 2 produeix un LRC incorrecte.

L'opció del decodificador **Incloure LRC calculat** afegeix el caràcter LRC imprimible a la sortida. La seva descomposició també mostra el patró de bits LRC amb paritat senar. Utilitza-ho per aprendre com un lector comprova el registre, no per eludir els controls de l'emissor.

## Escriure targetes sintètiques per a proves

**Utilitza el decodificador per escriure cadenes de prova, no targetes de pagament reals.** L'eina accepta camps, reconstrueix la Pista 1 i la Pista 2, afegeix sentinelles opcionals i calcula el LRC. Funciona localment al navegador.

1. Obriu el **[Decodificador i Codificador de Banda Magnètica](/magnetic-stripe-decoder/)**.
2. Seleccioneu **Carregar Targeta de Prova**. Això omple l'eina amb el PAN sintètic `4111111111111111`, el nom `TEST/USER`, la data de caducitat `2912`, el codi de servei `201` i dades discrecionals de prova.
3. Activeu **Incloure sentinelles d'inici i final** per mostrar els límits físics del registre.
4. Activeu **Incloure LRC calculat** per afegir el caràcter de verificació calculat.
5. Activeu **Dividir dades discrecionals en PVKI, PVV i CVV** només per veure com es mostra un camp sintètic de nou dígits. Aquestes etiquetes són convencions de l'emissor, no un format universal de Pista 1 o Pista 2.
6. Canvieu el nom, la data de caducitat, el codi de servei o les dades discrecionals sintètiques. La sortida s'actualitza mentre escriviu.
7. Compareu els camps decodificats amb les cadenes generades. Netegeu els camps quan acabeu.

Per a un exercici de Pista 1 sintètica, utilitzeu:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Per a un exercici de Pista 2 sintètica, utilitzeu el mateix PAN, data de caducitat, codi de servei i un camp discrecional numèric. La cadena generada de Pista 2 omet el nom perquè la Pista 2 no té camp de nom.

**No copieu un PAN, data de caducitat, CVV o valor discrecional real de Privacy.com a una targeta escrivible.** Privacy.com descriu el seu producte com a números de targeta virtuals creats a través del seu lloc web o aplicació. La seva pàgina oficial no presenta el servei com un sistema d'escriptura de banda magnètica, i un número de targeta virtual no és prova d'un registre físic autoritzat per l'emissor. Una targeta de prova escrivible que contingui una credencial real crea un instrument de pagament duplicat i viola els termes de l'emissor o les regles de pagament.

El límit segur és senzill: utilitzeu la mostra sintètica integrada de l'eina, utilitzeu una targeta de laboratori amb valors ficticis i utilitzeu una targeta física aprovada per l'emissor quan necessiteu pagar en persona. No intenteu convertir una targeta virtual de Privacy.com en una targeta física de banda magnètica.

## Què Canvia una Targeta Virtual

**Una targeta virtual és un segon número que substitueix el primer.**

Quan pagueu amb una targeta virtual, el comerciant rep un número, una data de caducitat i un CVV que pertanyen a la targeta virtual. El vostre PAN real mai no arriba a ells. Pràcticament, el canvi es fa evident després d'una filtració:

| Escenari | Amb la Vostra Targeta Real | Amb una Targeta Virtual Bloquejada per Comerciant |
|---|---|---|
| **Base de dades del comerciant filtrada** | El número és vàlid a tot arreu on s'accepta | El número falla a qualsevol altre comerciant |
| **Subscripció cancel·lada** | El càrrec continua fins que el disputeu | Tanqueu la targeta i el càrrec falla |
| **Prova que es converteix silenciosament** | Càrrec no desitjat al vostre extracte | El límit o el tancament ho atura |
| **Detalls de la targeta venuts en un fòrum** | Útil per frau sense presència de targeta | Útil només en un comerciant, si és que ho és |

**El que no canvia és igual d'important.** El vostre banc encara veu la transacció. La xarxa de targetes encara la processa. L'emissor encara té la vostra identitat, perquè les normes contra el blanqueig de diners requereixen verificació. **Una targeta virtual redueix l'exposició al costat del comerciant. No és una manera de gastar de forma anònima.**

*La distinció confon constantment la gent. Si el vostre model d'amenaça inclou l'emissor o la xarxa, una targeta virtual no canvia res d'això.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagrama que mostra un número de targeta virtual enviat al comerciant mentre el número real de la targeta es manté entre el titular i el banc emissor" >}}

## Els Tres Tipus de Objecte en Forma de Targeta

La terminologia s'utilitza de manera inconsistent i la diferència importa quan trieu què lliurar a un comerciant.

| Tipus | Número de Targeta | Versió Física | Ús Típic |
|---|---|---|---|
| **Targeta digital** | Igual que la vostra targeta física | Sí | Afegir la vostra targeta existent a una cartera mòbil |
| **Targeta virtual** | Diferent de qualsevol targeta física | No | Compres en línia, subscripcions, comerciants puntuals |
| **Targeta digital-primer** | Diferent, amb una targeta física vinculada opcional | Opcional | Comptes fintech on la targeta física no porta detalls impresos |

**Una cartera mòbil utilitza un quart mecanisme completament diferent.** Quan afegiu una targeta a una cartera, aquesta emmagatzema un token específic del dispositiu en lloc del vostre PAN, i el comerciant rep el token. Això s'anomena tokenització i és per això que pagar amb un telèfon és més segur que lliurar la targeta física, fins i tot sense una targeta virtual.

*La tokenització de xarxa i les targetes virtuals resolen parts superposades del mateix problema. La tokenització protegeix el número en trànsit i en repòs. Una targeta virtual us protegeix del que el comerciant conserva després.*

## Tipus de Targetes Privacy.com

**Privacy.com ofereix quatre comportaments de targeta, i no són intercanviables.**

| Tipus de Targeta | Comportament | Millor Per A |
|---|---|---|
| **D'Ús Únic** | Es tanca automàticament després d'una transacció | Compres puntuals i comerciants desconeguts |
| **Bloquejada per Comerciant** | Es bloqueja al primer comerciant que la carrega i falla en altres llocs | Compres en línia diàries |
| **Bloquejada per Categoria** | Restrigida a una categoria de despesa | Contenir tota una classe de despesa |
| **A Tot Arreu** | Una targeta física amb el mateix model de protecció | Compres presencials |

**El bloqueig per comerciant és el mecanisme que aporta més valor.** Una targeta bloquejada falla en qualsevol comerciant que no sigui el primer on s'ha utilitzat, cosa que significa que una filtració en aquest comerciant fa que el número sigui inútil en qualsevol altre lloc.

**L'ús únic és l'opció més forta quan s'aplica.** Una targeta que es tanca després d'un càrrec no es pot reproduir i elimina la necessitat de recordar tancar-la després.

Dos detalls operatius que val la pena conèixer:

- **Les targetes compartides es bloquegen al primer comerciant on s'utilitzen**, així que compartir-la amb un familiar o empleat encara porta la restricció del comerciant.
- **Una targeta es posa en pausa en lloc de tancar-se.** La pausa és reversible, cosa útil quan voleu aturar una subscripció temporalment sense perdre les dades de la targeta.

## Límits i Controls de Despesa

**Cada targeta té un límit de despesa, que és un control separat del bloqueig per comerciant.**

| Control | Què Prevé |
|---|---|
| **Límit per transacció** | Un càrrec individual més gran del que heu autoritzat |
| **Límit mensual** | Càrrecs acumulats durant un període de facturació |
| **Pausa** | Qualsevol càrrec, de manera reversible |
| **Tancament** | Qualsevol càrrec futur, de manera permanent |

**Establiu tant un límit per transacció com un límit mensual en qualsevol targeta vinculada a una subscripció.** Un comerciant que augmenta el preu silenciosament arriba al límit en lloc del vostre saldo, i ho noteu per un càrrec fallit en lloc d'una línia que falta a l'extracte.

*El nostre **[Mòdul de Seguretat Financera Personal](/personal-security-course/personal-finance/)** situa això al costat de les congelacions de crèdit i la tokenització de targetes com els tres controls que limiten què pot accedir un comerciant compromès.*

## Plans i Què Desbloqueja Cada Un

Privacy.com ofereix un nivell gratuït juntament amb tres plans de pagament. Els preus i els límits de funcions canvien, així que confirma els termes actuals abans de subscriure't.

| Pla | Preu | Afegits Notables |
|---|---|---|
| **Personal (gratuït)** | 0 $ | Targetes virtuals, bloqueig per comerciant, límits de despesa, sense comissió en transaccions domèstiques |
| **Plus** | 5 $/mes | Targetes per categoria, notes a les targetes per organitzar la despesa |
| **Pro** | 10 $/mes | Reemborsament en compres qualificades, targetes físiques Everywhere |
| **Premium** | 25 $/mes | Tot el de Pro, amb el límit mensual de creació de targetes augmentat a 60 |

**El nivell gratuït cobreix el benefici principal de seguretat.** El bloqueig per comerciant, les targetes d’un sol ús i els límits de despesa són els mecanismes que redueixen l’exposició, i estan disponibles sense pagar. Els nivells de pagament afegeixen organització i comoditat més que protecció addicional.

**Les comissions per transaccions estrangeres varien segons el nivell.** El nivell gratuït cobra un 3% en transaccions estrangeres amb un mínim de 0,50 $, mentre que els nivells de pagament no.

## Què No Fa Privacy.com

**Ser clar sobre els límits és més útil que una llista de funcions.**

| Limitació | Detall |
|---|---|
| **No et fa anònim** | La teva identitat es verifica en registrar-te i l’emissor la conserva |
| **No amaga la transacció al teu banc** | El teu banc veu la transferència de fons i la xarxa veu el càrrec |
| **No construeix crèdit** | No són comptes de crèdit i no es fa cap consulta de crèdit |
| **Només és per a EUA** | Requereix ciutadania o residència legal als EUA i un compte bancari o cooperativa de crèdit als EUA |
| **Requereix verificació d’identitat** | Els controls Know Your Customer són obligatoris segons les normes anti-blanqueig |
| **No cobreix tots els comerciants** | Alguns comerciants bloquegen rangs de targetes prepago i virtuals |

**El punt del bloqueig per comerciant és important en la pràctica.** Alguns serveis de subscripció i companyies aèries rebutgen rangs de targetes que associen amb targetes virtuals o prepago, i cap configuració soluciona el problema. Mantingues una targeta real disponible com a recurs per a aquests casos.

*El resum honest: una targeta virtual és un control de contenció per a l’exposició al costat del comerciant, no una eina d’anonimat. Si necessites anonimat, és un problema diferent amb eines diferents.*

## Qui Emet la Targeta i Per Què Importa

**Una targeta virtual continua sent una targeta real, emesa per un banc real, sota una llicència de sistema real.**

| Detall | Valor |
|---|---|
| **Banc emissor** | Patriot Bank, N.A., Membre FDIC |
| **Llicències de sistema** | Mastercard i Visa |
| **On s’accepta** | A qualsevol lloc on s’accepti Mastercard i Visa |
| **Finançament** | Transferit des del teu compte corrent vinculat als EUA |

**Per això la protecció és genuïna.** La targeta té les mateixes proteccions del sistema que qualsevol altre producte Mastercard o Visa, cosa que significa que s’apliquen normalment els drets de devolució i els processos de disputa per frau. No és una targeta regal ni un crèdit tancat de botiga.

Val la pena esmentar dues certificacions perquè són verificables de manera independent i no només afirmacions de màrqueting:

- **Compliment PCI-DSS**, que és l’estàndard de la indústria de targetes de pagament per al maneig de dades del titular de la targeta
- **SOC 2 Tipus II**, que és un informe auditat que cobreix controls de seguretat durant un període de temps i no una afirmació puntual

**Sobre el model de negoci:** l’empresa declara que guanya intercanvi dels comerciants i no ven dades de clients a anunciants ni tercers. Aquest és el mateix model d’ingressos que qualsevol altre emissor de targetes, i val la pena entendre-ho en lloc de considerar-ho inusual.

*La raó pràctica per comprovar el banc emissor és la verificació. Qualsevol pot afirmar que gestiona un programa de targetes, i el nom de l’emissor a la targeta és el que confirmes amb el banc indicat en la documentació.*

Inspecciona el sistema i el banc pel prefix PAN amb el **[Magnetic Stripe Decoder](/magnetic-stripe-decoder/)**, que informa del rang principal del sistema i valida el dígit de control Luhn.

## Com Utilitzar Bé les Targetes Virtuals

**Els controls només ajuden si els configures.** Sis hàbits aporten la majoria del benefici.

1. **Bloqueja cada targeta a un comerciant** tret que hi hagi un motiu per no fer-ho. El bloqueig és el que fa inútil un número filtrat.
2. **Utilitza targetes d’un sol ús per a qualsevol cosa desconeguda**, incloent proves i compres puntuals en llocs petits.
3. **Estableix ambdós límits de despesa** en targetes de subscripció, així un augment de preu falla en lloc de carregar.
4. **Anomena cada targeta pel comerciant**, perquè la llista de transaccions sigui llegible i un càrrec inesperat destaqui.
5. **Pausa en lloc de tancar** quan planegis reprendre un servei, i tanca quan no ho faràs.
6. **Mantingues una targeta real per a comerciants que rebutgen rangs virtuals**, perquè un bloqueig a la caixa no esdevingui una emergència.

> **Error comú: tractar una targeta virtual com a substitut de revisar els teus extractes.** El bloqueig per comerciant evita una classe de danys. No detecta un compte compromès al teu banc, una transferència no autoritzada ni un càrrec fraudulent a la targeta real darrere.

## Conclusions Clau

- **Una targeta virtual canvia el número que el comerciant emmagatzema.** El teu PAN real mai els arriba, que és tot el mecanisme.
- **No fa la transacció privada.** El teu banc, la xarxa i l’emissor encara la veuen, i la verificació d’identitat és obligatòria.
- **El bloqueig per comerciant és la funció de més valor**, perquè un número filtrat falla en qualsevol altre comerç.
- **El nivell gratuït inclou els controls de seguretat.** Els plans de pagament afegeixen organització i comoditat més que protecció.
- **La banda magnètica emmagatzema dades de la targeta en text pla** i s’eliminarà abans del 2033, amb els bancs dels EUA deixant d’emetre-les el 2027.
- **El CVV no està a la banda**, per això un skimmer que copia les pistes encara no té el que molts comerciants en línia requereixen.
- **Alguns comerciants rebutgen rangs de targetes virtuals.** Mantingues una targeta real com a recurs.
- **Verifica el banc emissor** en lloc de confiar en una afirmació del programa de targetes, i comprova tu mateix el prefix PAN.

## Passos Següents

1. **Inspeccioneu les dades de la pista de la vostra pròpia targeta** i vegeu exactament què conté una banda magnètica: **[Decodificador i codificador de banda magnètica](/magnetic-stripe-decoder/)**
2. **Congeleu el vostre crèdit** si encara no ho heu fet, que és el control més fort contra el frau en comptes nous: **[Seguretat financera personal](/personal-security-course/personal-finance/)**
3. **Apliqueu la disciplina de classificació per nivells** per decidir quant esforç mereix segons la vostra situació: **[Llista de control prioritzada de seguretat personal](/articles/personal-security-checklist-prioritized-2026/)**
4. **Reviseu els plans i termes actuals de Privacy.com** abans de subscriure-us: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Comproveu si les vostres dades ja apareixen en una filtració** abans de suposar que no us afecta: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Llegiu la llista de control de seguretat de pagaments** per a la contraparte organitzativa: **[Llista de control de resposta a incidents](/checklists/incident-response-checklist/)**

## Referències

1. [Privacy.com - què són les targetes virtuals, bloqueig de comerciants i límits de despesa](https://www.privacy.com/virtual-card)
2. [Targeta digital - Viquipèdia, que cobreix targetes digitals versus virtuals, pistes de banda magnètica, codis de servei, paritat i LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - targetes d’identificació, targetes de transacció financera, estructura de dades de les pistes 1 i 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - disseny detallat dels camps de la pista, incloent sentinelles i codis de servei](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [Consell d’estàndards de seguretat PCI - requisits de l’entorn de dades del titular de la targeta](https://www.pcisecuritystandards.org/)
6. [Oficina de Protecció Financera del Consumidor - informes i puntuacions de crèdit](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Codificació de dades ANSI/ISO ALPHA, el conjunt de caràcters de la Pista 1 i taula de paritat](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caràcters ISO de targeta magnètica, conjunts de la Pista 1 i Pista 2 comparats](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Lectura de dades de targeta magnètica, guia pràctica amb escaneig en viu d’una targeta](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)
