---
title: "Com verificar els resultats, les fonts, les proves i els costos de la IA"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crea un registre d’acceptació d’un resultat d’IA amb comprovacions de fonts, abast dels fitxers, proves dels tests, privadesa i ús."
genre: ["Intel·ligència artificial", "Enginyeria del programari"]
tags: ["verificar els resultats de la IA", "verificació de dades amb IA", "revisió d’agent de programació", "proves de tests d’IA", "seguiment de costos d’IA", "revisió humana"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Un full de revisió compara una afirmació d’IA amb un fitxer font, un diff de codi, la sortida de les proves i el total d’ús"
coverCaption: ""
---

[Torna al curs Flux de treball pràctic amb IA](/effective-ai-course-start/)

**Accepta un resultat d’IA només després de comprovar les proves adequades a la tasca.** Una explicació ben presentada, una eina configurada i un indicador verd de proves responen preguntes diferents. Aquesta lliçó crea un únic registre de revisió per al laboratori del taller.

**Objectiu d’aprenentatge:** elaboraràs un registre d’acceptació de fonts, abast dels fitxers, proves, privadesa i ús.

## Idees clau

- **Comprovació de fonts:** compara una afirmació basada en fets amb una font actual i autoritzada.
- **Comprovació de l’abast:** inspecciona quins fitxers o sistemes han canviat.
- **Comprovació del comportament:** executa proves i casos manuals pertinents.
- **Comprovació de privadesa:** inspecciona quin material ha rebut l’eina o el proveïdor.
- **Comprovació de l’ús:** registra els tokens, les crides a eines i la tarifa emprada per calcular el cost.

## Abans de començar

**Requisits previs:** el laboratori del curs, `docs/requirements.md`, una instantània local de Git i la [lliçó de MCP](/articles/effective-ai-mcp-server-setup/) o l’alternativa del navegador. Reserva 40 minuts. La dificultat és intermèdia. Fes servir el laboratori que vas editar en la primera tasca amb un agent de programació. Si no vas fer l’edició, utilitza una extracció nova i marca les comprovacions de funcionalitat com a no implementades. La base sense canvis encara supera les dues proves originals.

## Comprovar una afirmació basada en fets

**Afirmació:** «Els valors d’estat aprovats són `open` i `pending`». Obre `docs/requirements.md`, revisió 1. Hi diu `open` i `done`. L’afirmació és falsa. Un to segur no canvia el requisit.

**Per a afirmacions sobre productes,** fes servir documentació oficial actual i registra’n el títol de la pàgina i la data de revisió. Una afirmació sobre un menú, un pla, una ordre o un límit de context caduca més de pressa que un principi general de flux de treball. La [documentació de Codex](https://learn.chatgpt.com/docs/codex/cli), la [documentació de Claude Code](https://code.claude.com/docs/en/overview) i la [documentació d’OpenCode](https://opencode.ai/docs/) descriuen les interfícies actuals.

| Afirmació | Font | Decisió |
|---|---|---|
| **`open` i `pending`** | Requisit del laboratori, revisió 1 | Rebutja-ho i substitueix `pending` per `done` |
| **El recompte sense filtre és 4** | Programa base i quatre entrades JSON | Comprova-ho executant el programa |
| **S’ha fet una lectura MCP** | Transcripció de les eines de la sessió | Accepta-ho només si es veu una crida a l’eina |

## Inspeccionar el canvi

**En una tasca de programació,** fes servir Git per enumerar els fitxers modificats i llegir el diff real. Un fitxer nou sense seguiment apareix a l’estat encara que no figuri en un diff normal; per tant, inspecciona totes dues coses.

```bash
git status --short
git diff -- task_report.py tests
```

**Abast esperat:** després de la tasca del filtre, només canvien `task_report.py` i les proves específiques. Un canvi a `tasks.json`, `docs/requirements.md` o a un fitxer de configuració ocult requereix una explicació i una revisió separada. Si no has fet cap edició, no hi hauria d’haver canvis.

## Provar el comportament

**Executa les mateixes comprovacions base i de funcionalitat** des de la carpeta extreta del laboratori. L’informe de finalització de l’agent ha d’indicar els resultats observats d’aquestes comprovacions.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**A la còpia editada,** les proves cobreixen els casos nous, els recomptes són 4, 2 i 2, i el valor no vàlid acaba amb un error clar i un codi de sortida diferent de zero. En una còpia inicial nova, només passen les dues proves base i el total és 4. Registra aquest estat inicial per separat.

**Una prova de funcionalitat fallida requereix diagnòstic.** Si `open` mostra 4, comprova si l’argument del filtre arriba a la funció de recompte i si el programa compara el camp `status` de la tasca. No descriguis una prova fallida com a superada perquè l’agent digui que ha acabat la implementació.

## Comprovar privadesa i accés

**Registra quins fitxers ha rebut l’agent.** El laboratori conté dades sintètiques i no té secrets. Un projecte real pot incloure credencials, dades de clients o documents privats. Abans de compartir una sortida, inspecciona els prompts, els registres, les captures i els diffs per detectar aquests valors.

**Una prova local només demostra el comportament local.** No demostra els permisos d’un compte al núvol, l’abast d’un servidor MCP ni el comportament d’un servei desplegat. Comprova cada límit a l’entorn on sigui rellevant.

## Registrar l’ús i els costos

**Els tokens mesuren el volum d’entrada i sortida del model.** Els quadres de control varien segons el producte, així que fes servir les xifres d’ús del teu proveïdor. Registra per separat les crides a eines i els càrrecs per imatges o entorns allotjats quan correspongui. Comprova les tarifes actuals abans de calcular una factura real.

**Obre la vista d’ús del compte que ha executat la tasca.** Registra els tokens d’entrada i sortida que s’hi mostren, el model, el període de facturació i qualsevol categoria d’entrada en memòria cau. En les subscripcions de ChatGPT o Claude, un límit o una quota d’ús no equival a un cost d’API per tasca. Per a una execució d’OpenCode amb API o proveïdor, consulta l’ús o la facturació d’aquest proveïdor i la tarifa actual. Si el producte no mostra tokens per tasca, escriu «no disponible» i no dedueixis un càrrec de la llargada del xat.

**Càlcul il·lustratiu, no és una tarifa de proveïdor:** 30.000 tokens d’entrada a 1 $ per milió costen 0,03 $. 5.000 tokens de sortida a 5 $ per milió costen 0,025 $. El cost combinat del model en aquest exemple és de 0,055 $, abans dels càrrecs d’eines o allotjament.

```text
cost d’entrada = tokens d’entrada / 1.000.000 × tarifa d’entrada
cost de sortida = tokens de sortida / 1.000.000 × tarifa de sortida
total = cost d’entrada + cost de sortida + càrrecs separats d’eines
```

**Una tasca delegada també consumeix tokens.** La delegació trasllada la sortida detallada fora de la conversa principal, però no fa que la feina sigui gratuïta. Compara el cost amb el valor de la comprovació independent.

**Mantén separades les categories de càrrecs.** L’entrada en memòria cau, l’entrada nova, la sortida, les crides a eines i l’execució allotjada poden tenir tarifes diferents. Aquest exemple només utilitza tarifes d’entrada nova i de sortida. No diu res sobre una factura de subscripció o un càrrec d’eina.

## Mantenir un registre d’acceptació

| Camp | Exemple omplert després de l’edició |
|---|---|
| **Font** | `docs/requirements.md`, revisió 1, llegit |
| **Fitxers modificats** | `task_report.py` i `tests/test_task_report.py` a `git status --short` |
| **Proves** | Han passat les proves base i les noves del filtre; registra el recompte observat |
| **Sortida manual** | S’han observat `Total tasks: 4`, `2` i `2`; valor no vàlid rebutjat |
| **Estat de la funcionalitat** | `--status open` i `--status done` implementats |
| **Privadesa** | Només fitxers sintètics |
| **Ús** | Registra les xifres del teu proveïdor, si estan disponibles |
| **Decisió** | Accepta només quan passin les comprovacions de font, diff, proves i privadesa |

**El teu artefacte:** copia aquest registre i omple’l després de la teva pròpia execució. Substitueix «observat» només per una sortida que hagis vist. Tria Accepta quan passin totes les comprovacions necessàries, Revisa quan l’ajust estigui acotat i Atura’t quan la font, l’abast o l’accés no siguin clars.

## Comprovar què has après

1. **Pregunta:** una base inicial superada demostra que existeix la funcionalitat sol·licitada? **Resposta:** No. Després de l’edició, prova el nou comportament d’acceptació.

2. **Pregunta:** què ha d’incloure un registre d’acceptació? **Resposta:** proves de les fonts, fitxers modificats, comprovacions de comportament, abast d’accés i ús observat.

## Solució de problemes

- **No hi ha cap font per a una afirmació:** marca-la com a no verificada i cerca una font autoritzada.
- **Les proves passen però la sortida és diferent:** afegeix un cas manual i inspecciona les dades.
- **Falta informació d’ús:** registra «no disponible» en lloc d’estimar un cost real.
- **El diff inclou dades privades:** deixa de compartir la sortida i elimina aquestes dades del registre de pràctiques.

## Passos següents

**Continua amb [Delegació d’agents](/articles/effective-ai-agent-delegation/)**. Per obtenir més detalls sobre costos i privadesa, llegeix [encaminament de proveïdors](/articles/openrouter-provider-routing-quality-cost/) i [límit de privadesa de la IA local](/articles/local-ai-privacy-boundary/).

**Navegació del curs:** [Anterior: Configuració de MCP](/articles/effective-ai-mcp-server-setup/), [Esquema del curs](/effective-ai-course-start/).
