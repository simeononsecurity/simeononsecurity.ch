---
title: "Com fer servir bé la IA: un flux de treball fiable per a principiants"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Aprèn un flux de treball d’IA repetible: defineix la tasca, aporta context pertinent, examina les proves i verifica el resultat abans d’utilitzar-lo."
genre: ["Intel·ligència artificial", "Productivitat", "Enginyeria del programari"]
tags: ["com fer servir bé la IA", "flux de treball d’IA", "IA per a principiants", "verificació de la IA", "planificació de tasques d’IA", "agents de programació"]
cover: "/img/cover/effective-ai-workflow-foundations.webp"
coverAlt: "Una persona revisa un pla de treball d’IA al costat d’uns quants fitxers font i resultats de proves"
coverCaption: ""
---

[Torna al curs Flux de treball pràctic amb IA](/effective-ai-course-start/)

**Fes servir la IA com un col·laborador del qual cal revisar els resultats.** Comença per definir el resultat, aporta només el material pertinent i compara la resposta amb la font. Aquesta lliçó presenta un flux de treball per a converses, recerca i codi.

**Objectiu d’aprenentatge:** redactaràs un correu corregit per al taller i un registre de revisió amb quatre comprovacions.

## Idees clau

- **Tasca:** anomena el resultat que necessites i els seus límits.
- **Context:** aporta els fitxers, fets i exemples pertinents.
- **Proves:** pregunta d’on provenen les afirmacions i els canvis importants.
- **Verificació:** comprova el resultat final, no la confiança de l’assistent.

## Abans de començar

**Requisits previs:** accés a qualsevol eina de xat amb IA i una tasca innòcua que ja coneguis. No cal codi ni un pla de pagament. Reserva 25 minuts. Nivell: principiant.

**Escenari de pràctica:** gestiones un taller comunitari fictici. Un esborrany de correu diu que la pròxima classe comença a les 18 h. L’horari aprovat diu que comença a les 19 h. Vols un correu corregit i un registre dels canvis. No facis servir dades reals de clients.

## Conèixer els elements

| Terme | Significat |
|---|---|
| **Model** | Programari que produeix text o un altre resultat a partir d’una entrada |
| **Xat** | Conversa amb el model, sovint amb fitxers i eines |
| **Eina** | Funció que invoca l’assistent, com ara cercar fitxers o consultar un calendari |
| **Agent** | Assistent que fa una tasca en diversos passos i crides a eines |
| **Font** | Registre que fonamenta un fet o una decisió |
| **Artefacte** | Fitxer, missatge, taula o canvi de codi que conserves |

**Un text fluid no és una prova.** L’assistent podria escriure una frase convincent a partir d’un horari antic. Tracta els registres font com a fets i la sortida de l’assistent com una proposta fins que la comprovis.

## Escriure un paquet de tasca

**Comença pel resultat.** Després indica la font i un criteri d’acceptació. La lliçó 4 amplia aquest patró amb un [paquet de tasca per a un agent de programació](/articles/effective-ai-task-packets/). Ara fes servir aquesta petició breu:

```text
Resultat: redacta un correu per anunciar el pròxim taller.
Font: l’horari aprovat de sota diu que la classe comença a les 19 h.
Esborrany per corregir: «La classe Introducció a la seguretat digital comença a les 18 h el 12 de novembre a la sala comunitària A.»
Públic: assistents inscrits.
Límits: conserva el lloc i la data. Només redacta.
Acabat quan: l’esborrany digui 19 h i indiqui el canvi factual.
Horari aprovat: Introducció a la seguretat digital, 12 de novembre de 2026,
19 h, sala comunitària A.
```

**El paquet separa les instruccions de les dades.** El text de les 18 h de l’esborrany és el que cal corregir. L’horari aprovat determina l’hora. L’assistent no té permís per enviar el missatge perquè només li demanes un esborrany.

**Tria una font abans de resoldre una discrepància.** Si un resum del xat repeteix les 18 h, preval l’horari aprovat. Si dos horaris aprovats discrepen, atura’t i pregunta al responsable quina versió s’aplica. No resolguis una discrepància entre fonts amb una resposta fluida.

## Seguir el cicle de quatre passos

1. **Especifica:** defineix l’artefacte desitjat i una comprovació clara.
2. **Aporta:** inclou la font pertinent i indica quin registre preval si hi ha conflicte.
3. **Inspecciona:** compara el resultat amb la font i busca detalls inventats.
4. **Verifica:** fes una comprovació directa i després accepta, revisa o atura’t.

**Per al correu del taller,** llegeix el resultat línia per línia. Comprova l’hora, la data, el lloc i el públic. Demana que elimini qualsevol número de sala o enllaç d’inscripció que no aparegui a l’horari. La llista de canvis ha de dir «hora corregida: de les 18 h a les 19 h».

**Esborrany d’exemple:**

```text
Assumpte: Introducció a la seguretat digital, 12 de novembre

Hola,

La classe Introducció a la seguretat digital comença a les 19 h
el 12 de novembre de 2026, a la sala comunitària A.

Ens agradarà veure-us.

Canvi factual: hora d’inici corregida de les 18 h a les 19 h.
```

**Registre de revisió d’exemple:** hora, correcte, les 19 h coincideixen amb l’horari. Altres fets, correcte, l’esdeveniment, la data i la sala coincideixen. Abast, correcte, és un esborrany. Llista de canvis, correcte, s’indica l’única correcció. Són comprovacions de l’exemple sintètic. La teva pròpia execució necessita una revisió pròpia.

| Comprovació | Criteri d’aprovació | Si falla |
|---|---|---|
| **Hora** | L’esborrany diu 19 h | Torna a consultar l’horari aprovat |
| **Altres fets** | Data i lloc coincideixen amb la font | Elimina els afegits sense suport |
| **Abast** | El missatge és un esborrany | Atura qualsevol enviament |
| **Registre** | La llista de canvis indica la correcció | Demana una comparació factual |

**Una comprovació correcta és una observació.** Que l’assistent digui «verificat» no és una comprovació. Compara tu el resultat amb l’horari aprovat o fes servir una comprovació independent de confiança.

**Defineix els límits d’acció.** Redactar un recordatori és reversible. Enviar-lo arriba als destinataris. Abans d’enviar res en una feina real, exigeix una aprovació separada i vigent i comprova els destinataris.

## Triar la quantitat d’IA adequada

**Fes servir una resposta de xat** per a un esborrany petit o una explicació. Fes servir un projecte quan diverses converses relacionades necessitin les mateixes instruccions i fitxers. Un agent de programació és útil si cal cercar en un repositori, editar i provar. Fes servir un altre col·laborador si una recerca o revisió independent redueix molts detalls a la conversa principal.

**Per a un sol correu del taller, tria una resposta de xat.** Si redactes recordatoris per a totes les classes, posa l’horari aprovat i les pautes d’estil en un projecte. Un agent de programació no aporta res a aquest correu perquè no es demana cap canvi al repositori.

**No deleguis una tasca poc clara.** Cada col·laborador addicional necessita una pregunta delimitada i una manera de comprovar-ne el resultat. Les lliçons següents mostren quan el treball en paral·lel compensa.

## Practicar i comprovar

**El teu artefacte:** desa un paquet de tasca per a una tasca innòcua que controlis. Inclou el resultat desitjat, una font autoritzada, dos límits i una comprovació de finalització. Executa’l una vegada a l’eina de xat triada.

**Raonament esperat:** el resultat segueix la font indicada, respecta l’abast i exclou fets sense suport. Anota una correcció feta durant la verificació. Si no cal corregir res, registra quines línies de la font has comprovat.

**Criteri de finalització:** dona un punt per l’hora, els altres fets, el límit d’esborrany i una llista factual dels canvis. Acaba la lliçó amb quatre punts sobre quatre segons l’horari sintètic.

## Comprovar què has entès

1. **Pregunta:** quina font determina l’hora si l’historial del xat contradiu l’horari aprovat? **Resposta:** l’horari aprovat.
2. **Pregunta:** quines proves tanquen una tasca quan l’esborrany sembla plausible? **Resposta:** comprovació de la font, del resultat i de l’accés, i registre del resultat.

## Resolució de problemes

- **Resposta imprecisa:** concreta el resultat demanat i afegeix un exemple.
- **Detall inventat:** demana suport de la font i elimina el text sense justificació.
- **Resposta llarga:** fixa un límit de llargada o format al paquet.
- **Error repetit:** comença una conversa nova amb la font corregida i un resum breu.

## Passos següents

**Continua amb [Projectes de ChatGPT i Claude](/articles/effective-ai-chat-projects/)** per mantenir juntes les instruccions i els fitxers relacionats.

**Navegació del curs:** [Anterior: Configuració del curs](/articles/effective-ai-course-setup/), [Esquema del curs](/effective-ai-course-start/).
