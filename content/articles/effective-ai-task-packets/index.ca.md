---
title: "Paquets de tasques d’IA: millors instruccions i criteris d’acceptació"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Converteix les peticions vagues a una IA en paquets de tasques amb un resultat, una font, un àmbit de fitxers, comprovacions i una condició d’aturada definits."
genre: ["Intel·ligència artificial", "Productivitat", "Enginyeria del programari"]
tags: ["redacció d’instruccions d’IA", "paquet de tasques", "instrucció per a agent de programació", "criteris d’acceptació", "flux de treball d’IA", "instruccions per a agents d’IA"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Una petició vaga reformulada com un paquet breu de tasques amb font, àmbit, comprovació i condició d’aturada"
coverCaption: ""
---

[Torna al curs pràctic de fluxos de treball amb IA](/effective-ai-course-start/)

**Una bona instrucció descriu la feina i com n’avaluaràs el resultat.** Afegir paraules no resol la manca d’àmbit. Aquesta lliçó converteix una petició vaga en un paquet de tasques per al laboratori del curs.

**Objectiu d’aprenentatge:** escriuràs un paquet de tasques acotat amb font, àmbit de fitxers, comprovacions i una condició d’aturada.

## Idees clau

- **Resultat** indica l’artefacte o el comportament que vols.
- **Àmbit** indica els fitxers permesos i les accions excloses.
- **Font** identifica el requisit aprovat.
- **Criteris d’acceptació** fan que l’èxit sigui observable.
- **Condicions d’aturada** eviten conjectures i feina posterior no autoritzada.

## Abans de començar

**Requisits previs:** el laboratori extret, el seu fitxer `docs/requirements.md` i la [lliçó sobre el context del repositori](/articles/effective-ai-agents-md-context/). Reserva 30 minuts. El nivell és inicial. L’exercici acaba amb un paquet escrit. Encara no cal editar codi.

## Compara dues peticions

**Petició vaga:** «Millora l’script de tasques». Un agent podria reescriure la sortida, afegir dependències, editar dades d’exemple o ometre proves. La petició no defineix cap d’aquestes opcions.

**Petició acotada:** «Afegeix un filtre d’estat opcional a `task_report.py` segons la revisió 1 de `docs/requirements.md`. Conserva la sortida predeterminada. Afegeix proves. No canviïs les dades d’exemple. Atura’t abans del commit». L’agent encara decideix els detalls d’implementació, però la tasca defineix què vol dir tenir èxit.

| Part del paquet | Exemple del laboratori | Comprovació |
|---|---|---|
| **Resultat** | Afegir `--status` a l’informe | Funcionen els dos valors acceptats |
| **Font** | `docs/requirements.md`, revisió 1 | El codi coincideix amb els valors aprovats |
| **Àmbit** | Només el programa i les proves | El diff no inclou cap altre fitxer |
| **Restriccions** | Conservar la sortida predeterminada i les dades d’exemple | La sortida inicial continua sent `Total tasks: 4` |
| **Evidència** | Ordre de prova i execucions manuals | Les sortides coincideixen amb els recomptes previstos |
| **Aturada** | No fer commit ni push | L’historial de Git i el remot no canvien |

## Utilitza una plantilla reutilitzable

**Copia aquesta plantilla** per a una tasca petita de programació o recerca. Elimina els camps que no hi tenen relació en comptes d’omplir-los amb text vague.

```text
Resultat:
Font autoritzada i revisió:
Fitxers o registres rellevants:
Canvis permesos:
Canvis i accions exclosos:
Exemples del comportament desitjat:
Comprovacions de finalització:
Quan aturar-se o preguntar:
Informa de:
```

**Per al laboratori,** el paquet complet queda així:

```text
Objectiu: afegeix un filtre --status opcional a task_report.py.
Font: docs/requirements.md, revisió 1.
Fitxers rellevants: task_report.py, tasks.json, tests/.
Canvis permesos: task_report.py i proves específiques.
Exclosos: tasks.json, dependències noves, commits i enviaments.
Exemples: sense filtre, mostra Total tasks: 4. open i done mostren 2 cadascun.
Comprovacions: executa les proves unitàries i quatre ordres manuals: sense filtre, open, done i un valor no vàlid.
El valor no vàlid ha de retornar un codi diferent de zero amb un missatge clar.
Atura’t o pregunta si hi ha conflicte de fonts, falta un fitxer o falla una prova inicial no relacionada.
Informe: fitxers modificats, ordres, resultats observats i qüestions pendents.
```

**A Windows,** fes servir `py -3` a les ordres del paquet si el teu entorn utilitza el llançador de Python.

**El paquet no prescriu cada línia de codi.** Deixa que l’agent triï una implementació petita i manté el resultat verificable.

## Afegeix exemples amb cura

**Un exemple precís redueix l’ambigüitat.** Els exemples `open` i `done` indiquen la sortida del fitxer proporcionat amb quatre tasques. No estableixen una regla general per a tots els fitxers. En un fitxer diferent, els recomptes depenen dels seus registres.

**Separa el que s’espera del que s’observa.** Abans d’executar el programa, `Total tasks: 2` és el resultat previst per a cada estat. Després de l’execució, la sortida del terminal és una observació. Si els valors difereixen, examina les dades i la implementació abans d’afirmar que ha funcionat.

## Practica una condició d’aturada

**Suposa que falta el fitxer de requisits.** El paquet l’anomena com a font aprovada. Atura’t i demana el requisit en comptes d’inferir els valors acceptats d’un xat antic o d’un problema d’exemple.

**Suposa que les proves inicials fallen abans d’editar.** Registra l’error i pregunta si primer cal corregir l’estat inicial. Una execució posterior correcta no permet saber si la diferència prové del filtre o de l’estat d’inici.

**Suposa que l’agent vol fer un commit.** El paquet exclou els commits. Demana-li que s’aturi després del diff i les proves. Tu decidiràs si un commit posterior encaixa en el flux del projecte.

## Revisa el paquet

**Dona un punt per cada resposta:** el resultat és concret? S’indica la font que regeix la feina? L’àmbit dels fitxers és clar? Hi ha almenys dues comprovacions observables? Hi ha una condició d’aturada? Una puntuació inferior a cinc vol dir que cal revisar el paquet abans de delegar-lo.

**El teu lliurable:** desa el paquet final i una explicació d’una línia d’una condició d’aturada. Dona’l a un agent de programació en la propera lliçó pràctica o respon manualment els resultats previstos a la ruta d’estudi.

## Comprova què has après

1. **Pregunta:** què fa que un paquet de tasques sigui verificable? **Resposta:** Una font, els fitxers permesos, comprovacions observables i una condició d’aturada.
2. **Pregunta:** què ha de fer un agent si la font no inclou un detall necessari? **Resposta:** Aturar-se i informar del detall que falta en lloc d’inventar-lo.

## Resolució de problemes

- **L’agent canvia massa coses:** indica els fitxers i les accions excloses al paquet.
- **L’agent fa massa preguntes:** proporciona la font que falta o un exemple concret.
- **L’agent afirma massa aviat que ha acabat:** demana les sortides observades de les ordres i inspecciona els fitxers.
- **El paquet és massa llarg:** substitueix el material copiat de la font pel camí i la revisió.

## Passos següents

**Continua amb [La teva primera tasca amb un agent de programació](/articles/effective-ai-coding-agent-first-task/)**. Utilitza el paquet per guiar un petit canvi al laboratori.

**Navegació del curs:** [Anterior: Context del repositori](/articles/effective-ai-agents-md-context/), [Esquema del curs](/effective-ai-course-start/).
