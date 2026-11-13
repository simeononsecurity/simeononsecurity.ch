---
title: "Projectes de ChatGPT i Claude: configura un context d’IA reutilitzable"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Configura projectes de ChatGPT i Claude amb instruccions clares, fitxers de referència actualitzats i una prova senzilla del context reutilitzat."
genre: ["Intel·ligència artificial", "Productivitat"]
tags: ["Projectes de ChatGPT", "Projectes de Claude", "instruccions de projectes d’IA", "context d’IA", "configuració de projectes de ChatGPT", "coneixement de projectes de Claude"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Dos espais de treball de projectes d’IA organitzats amb una fitxa de projecte, fitxers de referència i converses separades"
coverCaption: ""
---

[Torna al curs de flux de treball pràctic amb IA](/effective-ai-course-start/)

**Crea un projecte quan diverses converses comparteixin el mateix propòsit.** Desa les instruccions estables i els fitxers de referència aprovats en un sol lloc. Mantén cada conversa centrada en una tasca. Aquesta lliçó utilitza un taller comunitari fictici per practicar sense dades privades.

**Objectiu d’aprenentatge:** crearàs un projecte amb dues fonts controlades i en comprovaràs els fets en un xat nou.

## Idees clau

- **Les instruccions del projecte** defineixen un comportament reutilitzable per als xats relacionats.
- **Les fonts del projecte** contenen el material de referència que vols que consulti l’assistent.
- **L’historial de conversa** registra un intercanvi, però no substitueix una font aprovada.
- **Una prova en un xat nou** mostra si la configuració del projecte aporta prou context.

## Abans de començar

**Requisits previs:** un compte de ChatGPT o Claude i el paquet de tasques de la [lliçó 1](/articles/effective-ai-workflow-foundations/). Reserva 35 minuts. El nivell és inicial. Fes servir noms, dates i llocs inventats durant tota la pràctica.

**Crea dos fitxers petits** a l’ordinador. Obre un editor de text pla, enganxa cada bloc següent en un fitxer separat i desa’l amb el nom `.md` indicat. Els fitxers Markdown són text pla. `workshop-brief.md` especifica el públic i l’estil. `approved-schedule.md` conté el calendari oficial fictici.

```text
workshop-brief.md, revisió 1
Públic: persones inscrites a un taller introductori.
Estil: frases curtes i un to amable i factual.
No inventis preus, funcions d’accessibilitat ni detalls d’aparcament.
```

```text
approved-schedule.md, revisió 1
Marca de la font: WS-2026-11-12-R1
Esdeveniment: Introducció a la seguretat digital
Data: 2026-11-12
Inici: 7 p.m.
Lloc: Community Room A
```

## Configura ChatGPT

1. **Obre «Projects»** a la barra lateral de ChatGPT i crea un projecte anomenat `Workshop Practice`.
2. **Afegeix-hi els dos fitxers** com a fonts del projecte.
3. **Obre la configuració del projecte** i afegeix les instruccions següents.
4. **Revisa la configuració de memòria i de compartició** del teu compte i espai de treball abans d’afegir-hi material real.

```text
Fes servir approved-schedule.md per a les dades de l’esdeveniment.
Fes servir workshop-brief.md per al públic i l’estil.
Si falta una dada sol·licitada, demana la font o indica que es desconeix.
Redacta només esborranys. No els enviïs ni publiquis.
Enumera els canvis factuals després de cada esborrany revisat.
```

**Els projectes de ChatGPT agrupen xats, fitxers i instruccions relacionats.** La configuració i les funcions disponibles varien segons el pla i l’espai de treball. Si el procés de creació ofereix memòria només del projecte, tria-la per fer una prova d’aïllament neta. Amb la memòria predeterminada, un xat pot utilitzar informació externa als fitxers pujats. El marcador únic de sota ajuda a provar el fitxer sense tractar una resposta de la memòria com a prova que s’ha llegit el fitxer. Consulta la [guia oficial dels projectes de ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) per comprovar les opcions actuals de memòria.

## Configura Claude

1. **Obre «Projects»** a Claude i crea un projecte amb el mateix nom de pràctica.
2. **Afegeix-hi els dos fitxers** al coneixement del projecte.
3. **Defineix les mateixes cinc línies** com a instruccions del projecte.
4. **Inicia un xat nou dins del projecte** per provar la configuració.

**Aquests passos descriuen els projectes clàssics de Claude.** Anthropic està desplegant una beta separada de Projects a alguns usuaris Pro i Max de Claude Code. A la beta, un projecte és una conversa amb fils paral·lels al núvol. Consulta [Què són els projectes?](https://support.claude.com/en/articles/9517075-what-are-projects) i segueix la interfície del teu compte. Les instruccions dels projectes clàssics s’apliquen a tots els xats, i el coneixement del projecte aporta material de referència compartit. Utilitza els fitxers pujats com a dades controlades. El funcionament de la memòria del projecte depèn del compte i de la configuració, així que no tractis els detalls d’un altre xat com el calendari aprovat. Consulta la [guia de configuració de projectes de Claude](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) per veure les opcions actuals.

| Mode del projecte | Material compartit que cal revisar | Prova nova |
|---|---|---|
| **Projecte de ChatGPT** | Fitxers pujats, instruccions i mode de memòria seleccionat | Un xat nou del projecte cita el marcador del calendari |
| **Projecte clàssic de Claude** | Coneixement i instruccions del projecte compartits entre xats | Un xat nou del projecte cita el marcador del calendari |
| **Beta de Claude Projects** | Fonts i context del projecte i dels fils al núvol | Un fil nou del projecte cita el marcador del calendari |

**Un projecte agrupa context, però no aprova cap font.** El marcador indica si el fitxer esmentat ha arribat al xat. Compara igualment la data, l’hora i la sala amb el fitxer.

## Prova un xat nou

**Obre una conversa nova d’un projecte de ChatGPT o un xat nou d’un projecte clàssic de Claude.** A la beta de Claude Projects, fes servir un fil nou del projecte. Demana un anunci breu. No incloguis el calendari al prompt, perquè les fonts del projecte n’aportin les dades.

```text
Redacta un correu de 100 paraules per al proper taller.
Indica el fitxer font i el seu marcador exacte per a l’hora i el lloc.
Enumera les dades que falten després de l’esborrany.
No enviïs el missatge.
```

| Resultat | Significat | Pas següent |
|---|---|---|
| **L’hora, el lloc i el marcador coincideixen** | El fitxer és accessible al xat | Comprova personalment les dades al fitxer |
| **S’ha inventat una dada** | Han fallat les instruccions o l’ús de la font | Elimina la dada i concreta la petició |
| **No hi ha la font** | La referència no ha arribat a aquest xat | Revisa la pertinença al projecte i la pujada del fitxer |
| **Apareix una revisió antiga** | El projecte conté material desactualitzat | Substitueix la font i repeteix la prova |

**No dedueixis la fiabilitat d’una sola resposta correcta.** La memòria predeterminada del projecte pot aportar una hora coneguda sense llegir el fitxer pujat. Exigeix el marcador exacte `WS-2026-11-12-R1` i repeteix la prova amb aquest esborrany contradictori:

```text
Revisa aquesta frase segons el calendari aprovat del projecte:
«La classe d’Introducció a la seguretat digital comença a les 6 p.m. a Community Room A.»
Indica el canvi factual, el fitxer font i el marcador. No enviïs el missatge.
```

**Resposta esperada:** la línia indica les 19 h i anomena `approved-schedule.md` amb el marcador `WS-2026-11-12-R1`. Anota qualsevol error que observis. Una prova superada no necessita cap error inventat.

**Exemple de registre de prova:** xat nou, primer prompt, hora 19 h, lloc Community Room A, font `approved-schedule.md`, marcador `WS-2026-11-12-R1`, superada. Prompt de conflicte, correcció de les 18 h a les 19 h, superada. Aquest és un exemple. Substitueix-lo per les teves observacions.

## Mantén el projecte

**Mantén breus les instruccions del projecte.** Desa-hi les regles estables. Inclou els detalls específics de cada tasca al seu prompt. Substitueix els fitxers desactualitzats i identifica’n les revisions. Separa la feina no relacionada en un altre projecte per evitar conflictes entre fonts.

**Abans de compartir un projecte,** revisa’n els fitxers, xats, instruccions i llista d’accés. Un projecte és un espai de treball, no un sistema d’aprovació. Fins i tot un fitxer anomenat «approved» necessita un responsable real i un registre de revisions per a la feina important.

## Practica i comprova

**El teu resultat:** un projecte amb dos fitxers de font sintètics, cinc línies d’instruccions i un registre breu de la prova. Anota l’hora i el lloc observats, el nom i el marcador de la font, i qualsevol dada inventada. Quan acabis, elimina el projecte de pràctica si ja no el necessites.

**Raonament esperat:** un xat nou utilitza les fonts del projecte per als fets estables, mentre que el prompt defineix el resultat immediat. Comprova la resposta al fitxer. Si falta una font o apareix una revisió incorrecta, torna a configurar el projecte.

## Comprova què has après

1. **Pregunta:** un xat nou d’un projecte de ChatGPT garanteix l’aïllament amb qualsevol configuració de memòria? **Resposta:** no. Revisa el mode de memòria del projecte i prova’l amb un marcador de font únic.

2. **Pregunta:** què has de fer si el projecte repeteix un calendari antic? **Resposta:** revisa la font adjunta i l’abast de la memòria, i després substitueix el material desactualitzat.

## Resolució de problemes

- **Falten controls del projecte:** consulta el teu pla actual i la configuració de l’espai de treball a la guia del proveïdor.
- **Respostes contradictòries:** elimina els fitxers de font duplicats o desactualitzats i inicia un xat nou.
- **Compartició inesperada:** revisa els membres del projecte i elimina les fonts sensibles abans de continuar.
- **Desviacions d’estil repetides:** escurça les instruccions i proporciona un exemple breu al prompt de la tasca.

## Passos següents

**Continua amb [Context del repositori AGENTS.md](/articles/effective-ai-agents-md-context/)**. La lliçó següent passa d’un projecte de xat a un repositori de codi local.

**Navegació del curs:** [Anterior: Fonaments del flux de treball](/articles/effective-ai-workflow-foundations/), [Esquema del curs](/effective-ai-course-start/).
