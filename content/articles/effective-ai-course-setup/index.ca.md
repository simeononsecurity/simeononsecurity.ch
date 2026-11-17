---
title: "Configuració del curs de fluxos de treball amb IA: terminal, Git i laboratori pràctic"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Prepara un espai segur per practicar amb IA, aprèn els termes de terminal i Git del curs i executa el laboratori inicial."
genre: ["Intel·ligència artificial", "Enginyeria del programari", "Educació"]
tags: ["configuració del curs d’IA", "conceptes bàsics de terminal", "conceptes bàsics de Git", "requisits previs d’agents de programació", "laboratori pràctic d’IA", "curs d’IA per a principiants"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Espai de pràctica per a principiants amb símbols de terminal, Python i Git, una carpeta de laboratori marcada i un arxiu per restablir"
coverCaption: ""
---

[Torna al curs pràctic de fluxos de treball amb IA](/effective-ai-course-start/)

**Prepara un espai segur abans d’utilitzar un agent.** Les lliçons 1 i 2 funcionen en un navegador sense aquest laboratori. Torna aquí abans de la lliçó 3 si vols completar tot el curs. Les lliçons pràctiques de programació fan servir Git, Python 3.10 o posterior i un agent de programació. El recorregut d’estudi substitueix les accions no disponibles de l’agent per tasques manuals indicades.

**Objectiu d’aprenentatge:** executaràs el laboratori inicial, desaràs una base local i explicaràs com restablir una còpia prescindible.

## Idees clau

- **Recorregut amb navegador:** completa els exercicis de xat, planificació, comprovació de fonts i revisió a ChatGPT o Claude.
- **Recorregut local:** fes servir un terminal i el laboratori Python inclòs per als exercicis de programació.
- **Recorregut de restabliment:** extreu una còpia nova del laboratori si un exercici falla.
- **Regla de seguretat:** mantén els fitxers privats, els registres de clients i les credencials fora del laboratori.

## Tria el recorregut

| Recorregut | Què necessites | Què practiques |
|---|---|---|
| **Introducció amb navegador** | Navegador actual i un compte de ChatGPT o Claude | Lliçons 1 i 2, més el paquet de tasques de xat de la lliçó 1 |
| **Pràctica local** | Git, Python 3.10 o posterior, terminal i un agent de programació | Fitxers, diferències, proves i canvis de l’agent |
| **Curs d’estudi** | Navegador, Python 3.10 o posterior local i Git | Totes les comprovacions del laboratori; els passos no disponibles d’agent i MCP s’indiquen com a no executats |

**Cada producte defineix els seus plans i límits.** Consulta [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) i [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) abans de dependre d’una funció. El recorregut d’estudi no demostra habilitat pràctica amb un agent de programació no disponible. Anota aquesta diferència a les notes de finalització.

**Segueix una ruta predeterminada:** fes servir ChatGPT en un navegador per als exercicis de xat i, després, un agent de programació disponible amb el laboratori local. Claude és una opció equivalent per al xat. Codex CLI, Claude Code CLI i OpenCode són opcions per a l’etapa de programació. No necessites comptes de tots els proveïdors.

**Anota cinc comprovacions abans d’obrir un agent de programació.** Això diferencia una comprovació del laboratori local d’una afirmació sobre un compte o un espai de treball allotjat.

| Comprovació | Anota |
|---|---|
| **Espai de treball** | Carpeta exacta del laboratori extret que llegirà l’agent |
| **Execució** | Ordinador local o espai remot seleccionat |
| **Proveïdor** | Compte o proveïdor del model emprat en aquesta tasca |
| **Permisos** | Si es permet escriure fitxers i executar ordres shell, o cal aprovació |
| **Base** | Nombre observat i dues proves aprovades abans dels canvis |

**Limita l’arrel de pràctica.** Un espai allotjat necessita la seva pròpia còpia del laboratori sintètic. Una execució local no demostra que la còpia remota o el compte tinguin els mateixos fitxers i permisos.

## Aprèn els termes locals

| Terme | Significat senzill |
|---|---|
| **Terminal** | Aplicació on escrius ordres |
| **Shell** | Programari que interpreta aquestes ordres |
| **CLI** | Interfície de línia d’ordres d’un programa |
| **Directori de treball** | Carpeta que una ordre fa servir per defecte |
| **Repositori** | Projecte que Git manté sota seguiment |
| **Commit** | Instantània desada de Git |
| **Branca** | Línia de canvis de Git amb un nom |
| **Diferència** | Vista de les línies afegides o eliminades |
| **Prova** | Comprovació repetible del comportament esperat |
| **Codi de sortida** | Nombre que indica l’èxit o el fracàs d’una ordre |

**No necessites GitHub per al laboratori inicial.** Git funciona a l’ordinador. GitHub és un servei d’allotjament independent. Un commit local desa una instantània sense enviar els fitxers enlloc.

## Prepara el laboratori

**Baixa el [laboratori inicial del curs](/downloads/effective-ai-course-lab.zip)** i extreu-lo en una carpeta nova que controlis. Obre-hi un terminal. A macOS o Linux, obre Terminal i fes servir `cd` per entrar a la carpeta extreta. A Windows, usa PowerShell o Windows Terminal i `cd`. A Windows, l’ordre Python sovint és `py -3` en comptes de `python3`.

**Instal·la [Python 3.10 o posterior](https://www.python.org/downloads/) i [Git](https://git-scm.com/downloads) si cal.** Comprova les eines instal·lades abans d’executar el laboratori. Les dues primeres ordres mostren versions. `cd` canvia el directori de treball i `ls` enumera els fitxers. Substitueix la ruta d’exemple per la ruta real de la carpeta extreta.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**A Windows PowerShell,** fes servir `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` i `Get-ChildItem`. La llista hauria d’incloure `task_report.py`, `tasks.json`, `tests` i `docs`. Si falla una ordre de versió, acaba d’instal·lar l’eina abans de continuar.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**A Windows PowerShell,** substitueix `pwd` per `Get-Location` si ho prefereixes, i `python3` per `py -3` si Python utilitza el llançador. La primera ordre mostra la ruta, que ha d’acabar amb la carpeta extreta del laboratori. Revisa també els noms. `AGENTS.md.txt` no serveix com a `AGENTS.md`. A l’Explorador de fitxers, activa les extensions per veure el nom complet.

**Resultat esperat:** l’informe diu `Total tasks: 4`. L’ordre de proves anomena dues proves i acaba amb `OK`. Un shell retorna el codi zero quan té èxit. Un altre recompte o un traceback vol dir que has de revisar la carpeta i la configuració de Python.

**Llegeix cada ordre per parts.** A `python3 task_report.py tasks.json`, `python3` inicia Python, `task_report.py` és el programa i `tasks.json` identifica les dades d’entrada. El recompte imprès és una sortida, no una altra ordre. Després d’un error, macOS i Linux mostren l’estat amb `echo $?`. PowerShell exposa l’estat de l’últim programa natiu amb `$LASTEXITCODE`.

**Reserva uns deu minuts per a la primera execució** després d’instal·lar Python: extreu el laboratori, executa l’informe i compara el total amb les quatre entrades de `tasks.json`. Obre el JSON en un editor de text i compta-les tu mateix.

## Practica Git amb seguretat

**Inicia Git només dins la carpeta extreta del laboratori.** Aquestes ordres desen una instantània local. `git status` mostra els fitxers canviats. `git diff` mostra les línies modificades després d’editar un fitxer seguit.

```bash
git init
git add .
git commit -m "Base del laboratori del curs"
git status --short
```

**Estat esperat:** després del commit no apareix cap nom de fitxer. Si Git et demana un nom i un correu, configura una identitat només per al laboratori des d’aquesta carpeta i repeteix el commit. Canvia els exemples per valors privats. No enganxis dades d’identitat o credencials en un xat públic.

```bash
git config --local user.name "Alumne del curs"
git config --local user.email "learner@example.invalid"
git commit -m "Base del laboratori del curs"
git status --short
```

**Per restablir no cal cap ordre Git.** Desa les notes fora del laboratori, elimina la còpia de pràctica extreta i torna a extreure el ZIP original. Fes-ho si un canvi de la lliçó deixa el programa en un estat desconegut.

## Protegeix l’espai de pràctica

**Fes servir exemples sintètics.** No pugis documents privats a un projecte del curs. No posis claus d’API en instruccions, fitxers font, captures de pantalla o commits. L’accés de l’agent als fitxers i les ordres depèn dels permisos i de la carpeta oberta. Revisa tots dos punts abans de deixar-lo executar.

**Comprova la compartició abans de pujar fitxers.** Els membres del projecte podrien accedir-hi. Per a la feina real, segueix la política de la teva organització. El curs usa dades fictícies, de manera que el laboratori no necessita cap aprovació especial.

## Practica i comprova

**El teu resultat:** anota el recorregut triat, els cinc camps previs, el recompte de l’informe, el resultat de les proves i el mètode de restabliment. Fes servir una còpia nova per confirmar que saps restablir el laboratori.

**Raonament esperat:** saps quina carpeta afecten les ordres, distingeixes Git local de l’allotjament i tens una manera de recuperar-te abans que un agent editi fitxers.

## Comprova què has entès

1. **Pregunta:** Una introducció només amb navegador completa el recorregut del laboratori local? **Resposta:** No. El recorregut complet necessita una base local de Python i Git.

2. **Pregunta:** Què has de desar abans de canviar el laboratori prescindible? **Resposta:** El resultat aprovat de la prova inicial i un punt de restabliment net.

## Resolució de problemes

- **No es troba l’ordre Python:** instal·la Python 3 des del distribuïdor oficial i torna a obrir el terminal.
- **No es troba el fitxer:** comprova el directori de treball i enumera els fitxers extrets.
- **Les proves no s’executen:** utilitza exactament l’ordre del README del laboratori extret.
- **Git demana una identitat per al commit:** configura Git localment i mantén els valors fora de les notes del curs.

## Passos següents

**Continua amb el [flux de treball d’IA fiable](/articles/effective-ai-workflow-foundations/)**. El primer exercici utilitza el mateix taller sintètic abans que cap eina rebi fitxers reals.

**Navegació del curs:** [Esquema del curs](/effective-ai-course-start/).
