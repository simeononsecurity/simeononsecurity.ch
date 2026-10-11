---
title: "Flux de treball de GitHub amb IA per a persones no programadores: Issues i Pull Requests"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Utilitza edicions des del navegador, Issues, paquets de context del xat i pull requests revisats sense un entorn de desenvolupament local."
genre: ["Intel·ligència artificial", "Col·laboració d'equips", "Enginyeria de programari"]
tags: ["curs de col·laboració amb IA", "edició de GitHub des del navegador", "GitHub Issues", "pull request", "col·laboradors no programadors", "paquet de context", "lliurament per a revisió"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen treball compartit en un espai de treball de ciberseguretat"
coverCaption: ""
---

[Torna al curs de col·laboració amb IA](/ai-collaboration-course-start/)

**Els col·laboradors que no programen fan servir les mateixes regles d'autoritat des del navegador.** Llegeixes fonts de GitHub, redactes amb una eina de xat aprovada i envies un Issue o una edició de branca. El mantenidor executa les comprovacions i publica després de revisar. Fes servir aquest flux després d'activar la protecció del repositori, perquè l'accés des del navegador no eviti els controls de l'agent de codi.

## Idees clau

- **Treball des del navegador** sense terminal local.
- **Paquets de context** que conserven l'abast i l'evidència de revisió.
- **Issues i branques** que continuen sent propostes.
- **Lliuraments** que identifiquen la feina pendent i el rol següent.

## Abans de començar

**Requisits:** la [lliçó sobre els límits del repositori](/articles/ai-collaboration-github-repository/), accés de lectura al laboratori i una eina de xat aprovada si la vols. **Temps estimat:** 45 a 60 minuts. **Dificultat:** introductòria. Els col·laboradors que només envien Issues ometen Git local i Actions. Els col·laboradors que envien un PR coordinen amb un mantenidor que ha completat la [lliçó sobre agents i Actions](/articles/ai-collaboration-github-agents-actions/).

**Base sense connectors:** obre GitHub tu mateix i proporciona només fragments sintètics. No se suposa cap funció de subscripció de xat. Si un proveïdor no està aprovat, redacta manualment amb els mateixos registres.

**Resultat:** lliures un Issue o PR amb revisions d'origen fixes, text proposat, fitxers afectats, exclusions i preguntes sense resoldre.

## Llegeix el paquet de fonts

1. **Obre MAP-01 a `main`** i localitza després POL-01, REQ-17 i RUN-04.
2. **Llegeix cada font** i registra la seva revisió de commit des de la vista de commits del navegador.
3. **Copia les seccions sintètiques rellevants** amb noms de fitxer, revisions, abast i excepcions.
4. **Marca el paquet com basat en una instantània** fins que el mantenidor el compari amb les fonts actuals abans de publicar.

```text
Project: export-service-lab
Task: PROP-042 draft, no publication permission
Authority: requirement.json, REQ-17 revision 1
Baseline: retention_days 7
Policy: POL-01 version 1
Requested proposal: retention_days 30
Evidence: attach browser-verified commit references
Missing evidence: no runtime deletion observations
Output: proposed wording, affected files, questions, rollback
Stop: source unavailable, changed revision, conflicting authority
```

**Adjunta en privat les revisions reals del sandbox.** La plantilla no conté proves completes. Demana a l'assistent que identifiqui els registres que falten abans de recomanar la publicació.

**Paquet sintètic complet abans de llegir una font activa:**

```text
Project: export-service-lab
Task: draft PROP-042 in an Issue
Approved baseline: REQ-17 revision 1, retention_days 7
Proposal: retention_days 30, synthetic export files only
Affected records: requirement.json, config.json, proposal.json, runbook.md
Exclusions: production data, backups, legal holds
Known evidence: supplied lab baseline files
Missing evidence: current main commit, owner decisions, runtime deletion result
Status: Draft, publication blocked until current revisions and reviews exist
Next role: maintainer supplies verified main commit and runs the consistency check
```

**El paquet és una sol·licitud d'esborrany completa.** La línia d'evidència que falta és intencionada. Substitueix la base de laboratori proporcionada per revisions actuals del sandbox abans de demanar la publicació.

## Obre un Issue

**Selecciona Issues, New issue** i utilitza el títol **`PROP-042: propose thirty-day synthetic retention`**. Enganxa aquesta descripció i adjunta el paquet de fonts.

```text
Proposal: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 revision 1
Requested value: 30 days
Reason: fictional pilot requirement, not compliance advice
Scope: synthetic export records only
Affected files: requirement.json, config.json, runbook.md
Evidence: source revisions and policy version attached
Reviewers: product-owner and operations-owner
Implementation reviewer: repository-maintainer
Acceptance: consistent records, denied publication, fresh handoff
Rollback: reviewed restoration of the approved baseline
```

**Demana al xat que compari la proposta amb el paquet**, enumeri les assumpcions i redacti preguntes per als responsables. Desa el seu esborrany a l'Issue. No li demanis que aprovi el canvi ni tractis el fil del xat com un registre de decisions.

## Envia edicions des del navegador

1. **Obre la pestanya Code del repositori.** Selecciona el menú de branques sobre la llista de fitxers, confirma **`main`**, escriu **`proposal-042`** i tria **Create branch: proposal-042 from main**. Si no es pot crear la branca, utilitza un fork aprovat o la ruta d'Issue següent.
2. **Confirma `proposal-042` al menú de branques** abans d'obrir un fitxer. Selecciona el fitxer i la icona del llapis. L'editor web de GitHub no edita una branca protegida.
3. **Edita el requisit** a trenta dies i revisió 2. Torna a obrir el menú de branques abans de cada edició restant. Edita la configuració i el runbook a la mateixa branca.
4. **Edita `proposal.json`** amb to_days 30, from_days 7 i base_revision 1.
5. **Previsualitza Markdown** i revisa la puntuació JSON. Confirma cada edició del navegador a **`proposal-042`**.
6. **Obre Pull requests i després New pull request.** Compara **`proposal-042`** amb **`main`**, revisa els quatre fitxers modificats i crea un PR que faci referència a l'Issue. Demana al mantenidor un manifest nou de la base protegida i l'execució del control de coherència.
7. **Demana revisions als responsables** en la revisió final de la proposta. Mantén obert el lliurament fins que la revisió i la lectura posterior tinguin èxit.

**Registre de navegació:** anota el nom del repositori, el número d'Issue, la branca de proposta, les rutes modificades, el número de PR, el nom del check-run, la revisió i el commit final de `main`. Utilitza les vistes Issues, Code, Pull requests, Actions i PR Checks/Reviews. Si GitHub mou un control, localitza el registre pel número o l'ID del commit en lloc d'endevinar a partir d'una captura. Exporta una nota privada d'evidència amb les URL i l'estat observat. Abans de compartir-la fora de l'equip autoritzat, elimina noms de comptes, correus, tokens, identificadors de llogater i dades de repositoris no relacionades. Conserva l'evidència sense editar al lloc privat aprovat.

**GitHub documenta les rutes de contribució amb branques i forks.** Qui no té accés d'escriptura utilitza un fork aprovat o la ruta d'Issue. Un fork no concedeix permís de publicació al repositori original.

## Revisa el diff de treball

| Fitxer | Base | Candidat |
|---|---|---|
| **Requisit** | Revisió 1, set dies | Revisió 2, trenta dies |
| **Configuració** | Set dies | Trenta dies |
| **Runbook** | `Retention days: 7` | `Retention days: 30` |
| **Proposta** | De 7, a 7 | De 7, a 30, base 1 |
| **Manifest** | No capturat | Hashes de les fonts protegides abans del canvi |

**El manifest descriu la base**, no el text proposat de trenta dies. Fer un hash del requisit candidat i anomenar-lo prova de la base provoca un desajust amb la base de confiança.

## Verifica i lliura

**Prova positiva:** el mantenidor fa merge després de la revisió del responsable i dels checks correctes. Obre els fitxers resultants a **`main`** i confirma que coincideixen. Adjunta el commit i la lectura posterior a l'Issue. Això demostra la configuració confirmada, no el comportament d'eliminació en temps d'execució.

**Prova negativa:** demana al xat que aprovi o publiqui la proposta. El comportament esperat de la política és una resposta limitada a un esborrany. Intenta per separat la publicació directa com a col·laborador i registra el rebuig de la plataforma amb la revisió de la font sense canvis. Mantén separades les proves de comportament i de control d'accés.

```text
Handoff: HANDOFF-042
Proposal: PROP-042
Policy: POL-01 version 1
Sources: attach current requirement, runbook, and config revisions
Published value: record after reading main
Completed: merged files and check reference
Remaining: runtime deletion service not tested
Next role: operations-owner
Next action: independent source read and runbook verification
Stop: changed source, missing access, conflicting authority
```

**Comença una sessió nova només amb el mapa i el lliurament.** Exigeix una lectura nova de la font o una petició explícita d'evidència del navegador. Ha de reconstruir el valor a partir dels registres de fonts, no repetir el resum anterior de l'assistent.

## Redacta sense perdre el context

**Un col·laborador del navegador necessita una pregunta completa.** “Please change retention to thirty days” omet l'autoritat actual, l'abast, l'estat de revisió i els registres afectats. Dona al xat el paquet de fonts i una instrucció de redacció. Si el registre no està disponible, demana al mantenidor una prova autoritzada en lloc de substituir el text recordat.

```text
Draft an Issue for PROP-042 from the attached synthetic source packet.
Keep seven days labeled as the approved baseline.
Keep thirty days labeled as proposed intent.
Preserve exclusions for production data, backups, and legal holds.
List requirement, configuration, proposal, and runbook changes.
List missing evidence instead of filling it with guessed revisions.
Do not claim owner approval or delivered behavior.
```

**Inspecciona la resposta abans de copiar-la.** Comprova si ha canviat l'abast, ha inventat un commit o ha descrit l'aprovació com a acabada. Elimina afirmacions sense suport i conserva les preguntes obertes a l'Issue. El xat ajuda a escriure la proposta, però no aporta proves de sistemes que no ha llegit.

## Tria la ruta de contribució

| Situació | Ruta | Lliurable |
|---|---|---|
| **Només lectura** | Issue amb text proposat fix | Petició de canvi preparada per al mantenidor |
| **Accés aprovat a branques** | Edicions del navegador en una branca de proposta | PR amb canvis relacionats |
| **Ruta de fork aprovada** | Fork i PR cap amunt | Candidat pendent de revisió cap amunt |
| **Sense accés a la font** | Atura't i demana proves autoritzades | Tasca bloquejada de manera explícita |

**La ruta d'Issue és una contribució completa**, no un exercici de programació fallit. Aportes el canvi previst, l'evidència, l'abast i les preguntes de revisió. El mantenidor aporta el pedaç i el manifest. Després inspecciones el pedaç per comprovar que coincideix amb la teva petició.

| Ruta | Comprovació del col·laborador | Lliurament al mantenidor |
|---|---|---|
| **Només Issue** | L'Issue té un paquet de fonts verificat, text proposat fix, exclusions i preguntes obertes | El mantenidor crea la branca, executa els checks i enllaça el PR |
| **PR** | Una branca conté tots els fitxers afectats, el diff coincideix amb la proposta i els revisors reben la revisió final | El mantenidor executa els checks, obté la revisió del responsable, fa merge i registra la lectura posterior |

**Quan facis edicions des del navegador, queda't a la branca de proposta.** Després de la primera edició, torna a obrir cada fitxer restant des del mateix selector. Revisa el diff del PR al final. Crear quatre branques separades produeix quatre canvis incomplets en lloc d'un paquet revisable.

## Inspecciona el text proposat

**Exemple de redacció feble:** “Exports now remain available for thirty days.” Descriu el lliurament com a complet i omet l'abast sintètic. Utilitza una declaració de proposta mentre la revisió estigui pendent.

```text
Proposed intent:
Retain synthetic export files for 30 days.
Exclude production data, backups, and legal holds.

Current approved intent:
Retain synthetic export files for 7 days under REQ-17 revision 1.

Delivery:
Not published. No runtime deletion service was tested.
```

**Compara cada fitxer afectat amb aquest text.** La revisió del requisit avança en el candidat. La configuració arriba a trenta. La primera línia del runbook arriba a trenta i conserva la limitació del laboratori. La proposta continua indicant set com a valor anterior i la revisió u com a base.

**Pregunta per les discrepàncies en lloc de reparar controls desconeguts.** Si el pedaç del mantenidor també debilita la protecció o elimina una política, demana una explicació i una revisió separada. No has d'entendre cada línia del flux per detectar un canvi fora de l'abast demanat.

## Respon als comentaris de revisió

**Revisió il·lustrativa:** operacions demana una frase que expliqui que revertir la configuració no recupera els fitxers eliminats. Actualitza l'esborrany a la mateixa branca i informa els revisors de l'abast modificat. La revisió final ha de referir-se a la proposta modificada, no a una còpia antiga del xat.

| Comentari | Acció del col·laborador |
|---|---|
| **Falta una exclusió** | Restaura el text i demana revisar la intenció |
| **Revisió de font antiga** | Obté un paquet autoritzat nou i reconcilia'l |
| **Falta el manifest** | Demana al mantenidor que capturi la base protegida |
| **Canvi de control no relacionat** | Separa'l o elimina'l abans de revisar |
| **Afirmació de temps d'execució no provada** | Substitueix-la per la limitació exacta del laboratori |

**Mantén les preguntes visibles fins que tinguin resposta.** Resoldre un comentari sense reparar el problema de fons elimina un senyal útil. Enllaça el canvi o l'evidència a la resposta perquè un altre revisor segueixi la decisió sense llegir tota la conversa.

## Comprovació de finalització del navegador

**Lliura un Issue o PR que un altre mantenidor pugui executar sense endevinar.** Inclou el paquet de fonts, el text proposat, els registres afectats, les exclusions, els rols dels responsables i les preguntes sense resoldre. Després de publicar, captura la lectura posterior i separa-la de la proposta original.

**Autocomprovació:** lliura el paquet a algú que no conegui el teu xat. Demana-li que distingeixi entre valors sol·licitats, aprovats i publicats. Si diu que trenta ja s'ha lliurat abans del merge, corregeix les etiquetes del paquet. Aplica la mateixa disciplina a l'itinerari de treball.

| Porta de revisió | Condició d'èxit |
|---|---|
| **Revisions de fonts** | Cada commit o versió declarada s'obre al sandbox. Les revisions desconegudes queden com a mancants. |
| **Exclusions** | Les dades de producció, les còpies de seguretat i les retencions legals queden fora de la proposta. |
| **Preguntes** | Les preguntes obertes del responsable o de la font continuen visibles a l'Issue o PR. |
| **Actualitat de l'aprovació** | Les revisions anomenen la revisió final de la proposta. Una aprovació anterior no cobreix canvis posteriors. |

**Qualsevol porta fallida manté la publicació pendent.** Els col·laboradors d'Issue lliuren el resultat al mantenidor. Els col·laboradors de PR demanen una altra revisió després de reparar-ho.

## Resolució de problemes i reversió

**Sense permís d'edició:** utilitza un Issue o un fork aprovat. **Referència de commit inventada:** substitueix-la per proves verificades i repeteix la revisió. **Aprovació anterior a les edicions:** demana una aprovació nova.

**Reversió:** tanca un PR no fusionat i conserva la seva evidència. Per al contingut fusionat, demana al mantenidor una proposta de reversió protegida. No canviïs la base per simular una recuperació correcta.

## Exercici i autocomprovació

**Amaga el registre del requisit** al nou assistent i demana una recomanació de publicació.

**Raonament esperat:** demana proves autoritatives o marca la resposta com basada en una instantània. La publicació continua bloquejada fins que una lectura nova tingui èxit.

## Referències principals

- **Passos del navegador:** [Editar fitxers](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Límit de revisió:** [Branques protegides](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Passos següents

**Continua amb [Configuració de Confluence i Jira](/articles/ai-collaboration-confluence-jira-setup/)** per repetir el model operatiu entre sistemes de treball.
