---
title: "Bucles d'agents d'IA acotats: comprovacions, reintents i regles d'aturada"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Defineix un bucle d'objectiu d'IA amb estat observable, comprovacions, límits de reintents, condicions d'aturada i un traspàs clar a una persona."
genre: ["Intel·ligència artificial", "Enginyeria del programari", "Productivitat"]
tags: ["bucles d'objectiu d'IA", "bucle de reintent d'agent", "regles d'aturada d'automatització d'IA", "monitoratge d'agents", "traspàs humà d'IA", "flux de treball d'IA acotat"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Un petit bucle d'agent que passa d'una edició a una prova, una decisió de reintent i un traspàs a una persona"
coverCaption: ""
---

[Torna al curs pràctic de fluxos de treball amb IA](/effective-ai-course-start/)

**Un bucle d'objectiu repeteix la feina fins que es valida un resultat definit o s'activa una regla d'aturada.** El bucle útil llegeix l'estat actual, fa una acció acotada, comprova el resultat i registra què ha passat. Una instrucció oberta com ara «continua provant» no té cap regla de finalització fiable.

**Objectiu d'aprenentatge:** executaràs un bucle de laboratori acotat amb una comprovació que se sap que falla i registraràs la decisió d'aturada.

## Idees clau

- **Objectiu:** un resultat formulat en termes observables.
- **Estat:** els fitxers, resultats, errors i revisió del codi font actuals.
- **Comprovació:** una prova o revisió vinculada a l'objectiu.
- **Pressupost de reintents:** el nombre màxim d'intents per a una fallada.
- **Regla d'aturada:** una condició que exigeix acabar o demanar una decisió a una persona.

## Abans de començar

**Requisits previs:** el [paquet de tasques](/articles/effective-ai-task-packets/), el [registre de verificació](/articles/effective-ai-output-verification/) i la [lliçó sobre delegació](/articles/effective-ai-agent-delegation/). Reserva 45 minuts. La dificultat és intermèdia. Fes servir una còpia nova del laboratori sintètic perquè la primera comprovació fallida sigui coneguda per endavant.

## Escriu el contracte del bucle

**Per a la petició de filtrar per estat**, defineix el contracte abans de qualsevol reintent:

```text
Objectiu: admetre --status open|done sense canviar la sortida predeterminada.
Font: docs/requirements.md, revisió 1.
Fitxers permesos: task_report.py i proves específiques.
Comprovacions: proves unitàries, recomptes 4/2/2 i codi de sortida no zero per a un valor no vàlid.
Pressupost de reintents: com a màxim dues edicions després del primer intent.
Atura’t immediatament: conflicte amb la font, canvi inesperat de fitxer, exposició d’un secret,
o fallada inicial no relacionada amb aquesta petició.
Traspàs: informa de la diferència final, les ordres, els resultats, els intents i el problema pendent.
```

**El pressupost és una política de la tasca**, no un valor predeterminat del producte. Dos reintents n'hi ha prou per diagnosticar una tasca petita de laboratori sense amagar fallades repetides. Una tasca de producció necessita una decisió pròpia sobre el risc i la revisió.

## Fes servir una taula d'estat

| Pas | Estat que cal registrar | Decisió |
|---|---|---|
| **Llegir** | Revisió del codi font i resultat inicial | Atura't si l'estat inicial és diferent |
| **Actuar** | Fitxers modificats i acció feta | Rebutja els canvis fora de l'abast |
| **Comprovar** | Prova exacta i resultat manual | Accepta o diagnostica |
| **Reintentar** | Causa de la fallada i hipòtesi nova | Continua només dins del pressupost |
| **Traspassar** | Estat final i responsable següent | Atura't després d'aprovar o quedar bloquejat |

**Registra els intents, no només l'últim missatge.** Una prova que acaba passant després de tres edicions ocultes no explica què ha canviat. Mantén un registre breu amb la fallada, la hipòtesi revisada i les proves noves.

## Analitza una fallada

**Primer intent il·lustratiu:** l'agent afegeix el filtratge i les proves. `open` mostra 2, però `--status invalid` mostra 0 i acaba correctament. El requisit exigeix que un valor no vàlid retorni un codi d'error diferent de zero. Marca la comprovació com a fallida.

**Diagnòstic:** inspecciona la validació dels arguments. L'agent ha tractat un valor desconegut com una coincidència buida en comptes de generar un error. Demana una correcció acotada per validar els valors acceptats abans de comptar. Torna a provar el cas invàlid i totes les comprovacions anteriors.

```text
Intent 1: l’estat no vàlid ha retornat èxit, així que l’acceptació ha fallat.
Causa trobada: no es validen els valors acceptats.
Petició de l’intent 2: rebutja els valors no admesos i conserva els recomptes 4/2/2.
Proves necessàries: execució completa de les proves i codi de sortida de l’ordre no vàlida.
```

**Resultat esperat del segon intent:** un error clar i un codi diferent de zero per a `invalid`, amb els recomptes vàlids sense canvis. Si el segon intent encara falla, fes servir l'últim reintent només després d'identificar una causa nova. Repetir la mateixa petició no és un diagnòstic.

## Gestiona resultats ambigus

**Que un procés s'aturi sense resultat no és un èxit.** Si una eina esgota el temps després d'una possible escriptura, inspecciona els fitxers i l'estat de Git abans de tornar-la a executar. Si un servei connectat informa d'un resultat desconegut, consulta'n l'estat actual abans de repetir una acció externa. Fora del laboratori, els enviaments, les publicacions o les escriptures duplicats són un risc real.

**Atura't i demana una revisió humana** si el requisit entra en conflicte amb una altra font aprovada, un permís impedeix l'acció, s'esgota el pressupost de reintents o l'acció sol·licitada supera el límit de publicació. El traspàs ha d'indicar l'estat exacte i la decisió pendent.

## Separa els bucles dels monitors

**Un bucle d'edició** s'executa dins d'una tasca acotada i comprova el resultat després de cada acció. **Un monitor programat** es desperta més tard per inspeccionar una condició. Un monitor necessita la seva pròpia freqüència, llindar de canvi, regla de notificació i condició d'aturada. No converteixis el bucle d'edició del laboratori en una tasca recurrent. La lliçó següent avalua els sistemes persistents abans d'activar-los.

## Executa un bucle controlat

**Comença amb el laboratori intacte.** Les dues proves inicials passen. Crea `tests/test_loop_contract.py` a l'extracció nova amb la comprovació següent. Aquest fitxer expressa una funció desitjada que no hi és a l'inici. No forma part del ZIP de laboratori mantingut.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Executa `python3 -m unittest discover -s tests -v`.** Les dues proves originals haurien de passar i la nova prova contractual hauria de fallar perquè el laboratori inicial no té `--status`. Registra la fallada real. Si has inicialitzat Git tal com s'indica a la lliçó 0, registra també `git status --short`. Si no, compara els fitxers modificats amb una extracció intacta. A Windows, fes servir `py -3` si la configuració utilitza el launcher.

**Defineix un pressupost de tres intents:** la primera edició i com a màxim dues correccions. Dona a l'agent el contracte del bucle anterior i demana una edició acotada. Després de cada intent, inspecciona els fitxers canviats, torna a executar totes les proves i executa les ordres predeterminada, `open`, `done` i invàlida. Registra la causa de la fallada abans d'un altre intent. Atura't si passa, si falla una comprovació inicial no relacionada, si hi ha un canvi fora de l'abast o si falla el tercer intent.

**Ruta d'estudi:** aplica la [resposta completa de la lliçó 5](/articles/effective-ai-coding-agent-first-task/) en aquesta còpia nova després de registrar la prova vermella. Torna a executar les mateixes comprovacions i marca que no s'ha executat l'edició de l'agent. Conserva la prova contractual controlada. No la debilitïs ni l'esborris per fer-la passar.

| Intent | Estat i observació | Decisió |
|---|---|---|
| **Abans de l'edició** | Les dues proves inicials passen i la nova comprovació `open` falla | Continua amb una edició acotada |
| **Després de cada edició** | Registra les proves exactes, els recomptes, el codi d'error per a un valor invàlid i els fitxers canviats | Accepta, diagnostica o atura't |
| **En esgotar el pressupost** | Registra la fallada pendent i la diferència actual | Traspassa la tasca sense un altre intent |

## Practica i comprova

**El teu artefacte:** la prova controlada que falla, els resultats observats abans i després, un registre d'intents i una decisió final d'acceptació o aturada. Si la primera edició passa, registra un sol intent. No inventis una segona fallada per omplir el registre.

**Comprovació de finalització:** el contracte especifica una font, l'abast dels fitxers, comprovacions observables, el límit de reintents, almenys una condició d'aturada immediata i un traspàs. El registre inclou la prova vermella real, els resultats posteriors i un resultat aprovat o una aturada per pressupost. Un segon intent identifica una causa nova i és diferent del primer.

## Comprova què has entès

1. **Pregunta:** què demostra la primera prova contractual vermella? **Resposta:** que el laboratori inicial no té el filtre d'estat que demana una prova escrita abans de l'edició.
2. **Pregunta:** quan s'ha d'aturar el bucle encara que quedin reintents? **Resposta:** quan hi ha un canvi fora de l'abast, un permís poc clar o un requisit en conflicte.

## Resolució de problemes

- **El bucle repeteix la mateixa fallada:** atura't i formula una hipòtesi nova sobre la causa.
- **Les comprovacions es debiliten:** restaura els criteris originals d'acceptació.
- **Resultat extern incert:** inspecciona l'estat actual abans d'un altre intent.
- **Pressupost esgotat:** traspassa el registre de fallades en comptes d'amagar-les.

## Passos següents

Continua amb l'opcional [Avaluació d'agents especialitzats](/articles/effective-ai-specialized-agent-evaluation/) o ves directament al [projecte final del curs de flux de treball amb IA](/articles/effective-ai-capstone/). Per explorar opcions d'entorn d'execució, llegeix la [guia d'entorns d'agents](/articles/best-ai-agent-harnesses/).

**Navegació del curs:** [Anterior: delegació d'agents](/articles/effective-ai-agent-delegation/), [Esquema del curs](/effective-ai-course-start/).
