---
title: "Flux de publicació amb IA a GitHub, Confluence i Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publica una proposta fixa de retenció a Confluence, GitHub i Jira amb comprovacions de versions i recuperació davant d'una publicació parcial."
genre: ["Intel·ligència artificial", "Col·laboració en equip", "Enginyeria del programari"]
tags: ["curs de col·laboració amb IA", "Confluence Cloud", "Jira Cloud", "publicació entre sistemes", "comprovació de versions", "registre de publicació", "publicació parcial"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen un projecte compartit en un espai de treball de ciberseguretat"
coverCaption: ""
---

[Torna al curs de col·laboració amb IA](/ai-collaboration-course-start/)

**El col·laborador fixa PROP-042 abans que els responsables l'aprovin.** Un publicador de Confluence actualitza els requisits, un mantenidor de GitHub fusiona la implementació i l'equip d'operacions publica el runbook. Jira registra cada pas. Fes-ho després de verificar els permisos, perquè els tres sistemes no formen una transacció atòmica. El teu registre de publicació fa visibles els lliuraments incomplets.

## Idees clau

- **La intenció aprovada** difereix del comportament lliurat.
- **Les revisions fixes de la proposta** vinculen la revisió a una versió.
- **Els registres de publicació** exposen els passos incomplets.
- **Les lectures recents** protegeixen davant de canvis en les bases.

## Abans de començar

**Requisits previs:** la [configuració de l'entorn de treball](/articles/ai-collaboration-confluence-jira-setup/), accés de publicació, responsables i un mantenidor del repositori. **Temps estimat:** dues hores. **Dificultat:** coordinació avançada.

**Interfície de referència:** lectures al navegador, redacció opcional en un xat aprovat i publicació humana. No es pressuposa cap subscripció a connectors. Abans d'afegir una integració, revisa'n la disponibilitat al tenant, els àmbits, el tractament del proveïdor i l'assignació d'identitats. No comparteixis mai les credencials d'un responsable amb un col·laborador.

**Resultat per al lector:** acabaràs amb una proposta fixa, un registre de publicació per sistema, proves de relectura i una decisió de recuperació per al primer pas incomplet. L'exercici demostra el procediment i el tractament de proves, no el comportament de retenció en producció.

## Registrar les fonts actuals

1. **Llegeix MAP-01** i després obre REQ-17 i RUN-04 amb els ID de pàgina assignats.
2. **Obre el menú de la pàgina i Page History** i registra les versions numèriques, l'estat, el text, el responsable i les excepcions.
3. **Llegeix l'element de Jira** i adjunta una exportació fixa de la proposta o un commit de GitHub. La clau per si sola no fixa les proves de revisió.
4. **Llegeix POL-01 aprovada** i la configuració de referència protegida.
5. **Proporciona al xat només els fragments sintètics necessaris**, marca'ls com a instantànies i mantén desactivades les accions d'escriptura.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Els paquets fora de línia continuen basant-se en instantànies.** El publicador torna a llegir les fonts actuals abans d'escriure. La denegació d'accés bloqueja la publicació. Una exportació antiga no substitueix l'autorització actual.

## Fixar la proposta

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Substitueix les versions il·lustratives de les pàgines per les versions que hagis capturat realment.** Adjunta a Jira el JSON fix i el text proposat. Cada responsable registra el seu rol, la decisió, la revisió de la proposta, les versions de les fonts i l'hora de la revisió. Qualsevol canvi substancial retorna el paquet a `Review`.

**Producte revisa la intenció i l'abast. Operacions revisa la neteja i la recuperació.** El mantenidor revisa el diff. Les reaccions a missatges de xat mutables no són aprovacions vinculades a una revisió.

## Publicar i tornar a llegir

1. **Mou Jira a `Publishing`** després que el publicador verifiqui les dues revisions dels responsables i que les bases d'origen no hagin canviat.
2. **Publica REQ-17** amb trenta dies i un camp de lliurament pendent. Registra la versió resultant, l'abast i les excepcions.
3. **Obre la PR d'implementació de GitHub**, amb referència a la versió aprovada de la pàgina. Canvia la configuració a trenta dies i adjunta una instantània no autoritativa del requisit.
4. **Fusiona després de la revisió del repositori** i torna a llegir **`main`**. Registra per separat el comportament desat al repositori i el comportament en execució.
5. **Publica RUN-04**, torna a llegir-lo per ID i registra la versió resultant. El publicador actualitza les referències de lliurament del requisit.
6. **Completa Jira** només quan tots els registres coincideixin i s'adjunti la prova de la lectura final.

**Utilitza el validador local només per comprovar la coherència de les instantànies.** Copia el requisit de Confluence anterior al canvi a l'esquema JSON de referència del laboratori, captura'l i edita la proposta perquè indiqui trenta dies. Incrementa la revisió local de la instantània i conserva per separat a Jira les versions reals de Confluence. El flux amb GitHub com a font arrel no valida el Confluence actiu. No presentis l'estat verd com una verificació d'autoritat externa.

**No despleguis funcionalitat d'eliminació en aquest exercici.** Un servei real necessita proves de desplegament, dades de prova controlades, un mecanisme per suspendre temporalment les eliminacions i proves dels límits en execució. Una fusió prova l'estat del repositori, no el comportament de retenció en producció.

## Seguir una publicació parcial

| Pas | Estat inicial | Prova de finalització |
|---|---|---|
| **REQ-17** | Pending | Versió resultant de la pàgina |
| **Configuració** | Pending | Commit fusionat i revisió |
| **RUN-04** | Pending | Versió resultant de la pàgina |
| **Tancament de Jira** | Pending | Lectura final i transició |

**Registra cada resultat abans d'intentar el pas següent.** PROP-042 correlaciona els esdeveniments de cada sistema. Una sola fila completada no vol dir que tot el canvi estigui complet.

**Fracàs il·lustratiu:** Confluence publica trenta dies, però GitHub denega la fusió. Mantén Jira en `Blocked` i el requisit marcat com a lliurament pendent. Producte tria completar el canvi o restaurar els set dies després d'una revisió. No converteixis una còpia d'emergència del README en l'autoritat del requisit.

## Gestionar edicions simultànies

**Referència del navegador:** designa un únic publicador durant la finestra del pilot. Torna a obrir Page History immediatament abans d'editar i després de publicar. Si una altra persona canvia la font, atura't, compara, concilia i renova l'aprovació. La publicació serialitzada és un procediment, no una garantia de transacció atòmica.

**Extensió de l'API:** la documentació de Confluence v2 descriu **`GET /wiki/api/v2/pages/{id}?body-format=storage`** i **`PUT /wiki/api/v2/pages/{id}`** amb un objecte de versió. Una integració de publicació revisada compara la versió actual amb la base aprovada, envia la versió següent i la torna a llegir. No actualitzis automàticament una versió fallida ni reintentis amb un cos antic.

**L'èxit de l'API per si sol no és suficient.** Comprova el contingut resultant, l'ID d'origen, l'abast i la versió. Aquest curs no inclou cap client d'API amb capacitat d'escriptura. La publicació humana al navegador és la referència executable per a qui no programa.

## Verificar casos negatius

| Injecció | Raonament esperat |
|---|---|
| **Canviar la font després de l'aprovació** | Aturar-se i tornar a aprovar la versió nova |
| **Treure l'accés d'edició del publicador** | Denegar l'actualització i mantenir el registre pendent |
| **Establir Jira en seixanta dies** | Aturar el conflicte i conservar l'autoritat de Confluence |
| **Fallada en la publicació del runbook** | Mantenir el lliurament incomplet i assignar la recuperació |

**Registra els resultats reals del sandbox** amb el rol de l'actor i les revisions abans i després. No incloguis el contingut protegit de la pàgina en proves per a usuaris sense accés. Els resultats esperats no són resultats mesurats.

## Muntar el paquet de revisió

**Fixa el contingut, no només l'etiqueta de la proposta.** PROP-042 apareix en cada sistema, però una etiqueta no identifica el contingut que ha revisat el responsable. Inclou en un únic paquet fix el text exacte del requisit, el diff d'implementació, el text del runbook, les versions de les fonts i la seqüència de publicació.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Fes que el paquet sigui llegible per als dos responsables.** Producte necessita la intenció i les exclusions. Operacions necessita el canvi operatiu i els límits de recuperació. Tots dos han d'entendre el període en què la intenció aprovada i la configuració lliurada difereixen. Un diff de codi sense més no és suficient per a un responsable que no coneix els fitxers del repositori.

**Contingut completat del paquet per a aquest exemple sintètic:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Aquestes frases són textos de proposta d'exemple, no registres d'un tenant actiu. Adjunta el commit de base real i les versions de les pàgines abans de la revisió. El paquet fix ha d'incloure tots els textos proposats, no un resum que obligui el responsable a deduir-los.

**Separa la instantània fora de línia de la publicació en directe.** Just abans de la primera escriptura, el publicador torna a comprovar les pàgines assignades i el mantenidor torna a comprovar la base protegida. Si alguna ha canviat, el paquet antic s'atura a `Review`.

## Recórrer el registre

**Progressió d'estat il·lustrativa:** la taula utilitza revisions didàctiques, no observacions. Omple les versions resultants i els commits reals després de cada escriptura al sandbox.

| Pas | Estat després d'una lectura correcta | Feina pendent |
|---|---|---|
| **Revisió dels responsables completada** | Paquet aprovat, tots els valors publicats són set | Tots els passos de publicació |
| **REQ-17 publicat** | Intenció de trenta, lliurament pendent | Configuració i runbook |
| **Fusió de GitHub tornada a llegir** | Intenció/configuració de trenta, runbook de set | Runbook i conciliació final |
| **RUN-04 publicat** | Tots els registres aplicables són trenta | Lectura final independent |
| **Lliurament tancat** | Registre complet amb proves | Les limitacions d'execució declarades continuen |

**El lliurament pendent és un estat significatiu.** Evita descriure la implementació antiga com a compatible amb la intenció nova mentre la publicació encara és incompleta. Durant aquest període, els lectors necessiten tots dos valors, no un resum únic que afirmi que la retenció és de trenta dies.

**Afegeix els intents fallits com a esdeveniments separats.** Si falla l'escriptura del runbook, conserva els resultats correctes del requisit i de la configuració. Registra l'acció intentada, la fallada, la versió inalterada, el rol assignat i l'acció següent. No tornis a posar les files completades en Pending ni esborris la seqüència observada.

**Exemple de rebuig per versió obsoleta:** el publicador llegeix REQ-17 v4, un altre editor autoritzat publica v5 i, després, el publicador intenta aplicar PROP-042 r1 sobre v4. La plataforma indica un conflicte de versions o la lectura prèvia a l'escriptura detecta v5. Registra l'actor `publisher`, la versió inicial `v4`, l'intent `PROP-042 r1`, el conflicte observat o el canvi de versió actual, la versió final `v5` que aquest intent no ha canviat i el responsable assignat `product owner`. Mantén Jira en `Review`. Torna a llegir v5, concilia el text i demana una revisió d'un paquet fix nou abans d'una altra escriptura. En una prova real, utilitza la resposta de la plataforma i Page History. Aquesta fila és un exemple didàctic.

**Exemple didàctic completat, només amb valors sintètics:**

| Sistema | Font inicial | Revisió fixa | Escriptura i relectura | Estat final |
|---|---|---|---|---|
| Confluence REQ-17 | v4, set dies | PROP-042 r1, Producte aprova de v4 a v5 | El publicador escriu v5, el revisor torna a obrir v5 | Trenta dies, exclou còpies de seguretat i retencions legals |
| Configuració de GitHub | Commit `main` `base-001`, set dies | PROP-042 r1, Operacions aprova el diff candidat | PR fusionada com a `merge-002`, clon independent llegeix trenta | Trenta dies a la font protegida |
| Confluence RUN-04 | v2, set dies | PROP-042 r1, Operacions aprova de v2 a v3 | El publicador escriu v3, el revisor torna a obrir v3 | Pas operatiu de trenta dies amb reversió |
| Jira PROP-042 | In Review | Les dues decisions dels responsables estan vinculades a r1 | El responsable del lliurament adjunta proves i passa a Done | Tancat després de les tres relectures |

Les etiquetes anteriors són il·lustratives, no proves del tenant. El teu registre necessita enllaços natius a les versions de les pàgines i ID de commit. Abans de passar Jira a Done, adjunta la proposta fixada, les dues revisions per rol, el registre de les bases d'origen, cada relectura de publicació, el resultat de la prova negativa i les limitacions d'execució no resoltes. Si falta algun element, mantén el lliurament obert o `Blocked`.

**Porta del paquet:** marca cadascuna de les cinc comprovacions com a `Supported` o `Blocked`: les revisions de les fonts són actuals, tots dos responsables han aprovat la mateixa revisió fixa, totes les publicacions necessàries coincideixen amb la relectura, les limitacions d'execució continuen explícites i l'estat de recuperació està conciliat. `Done` requereix cinc comprovacions `Supported` i cap escriptura no autoritzada.

## Gestionar una escriptura incerta

**Un timeout deixa el resultat desconegut.** No demostra ni l'èxit ni el fracàs. En el flux del navegador, torna a obrir la font assignada i inspecciona el contingut i l'historial actuals abans de decidir si ho tornes a provar.

1. **Posposa el pas següent:** mantén el lliurament incomplet.
2. **Llegeix la destinació:** compara el text actual, la versió i l'abast amb el paquet fix.
3. **Registra l'observació:** completada, sense canvis, conflictiva o inaccessible.
4. **Tria l'acció següent:** continua des d'una finalització verificada, torna a provar un pas autoritzat sense canvis o escala un conflicte.
5. **Conserva la incertesa:** mantén l'intent fallit/desconegut al costat de la relectura posterior.

**No repeteixis tota la seqüència a cegues.** Repetir un pas ja complet afegeix revisions i arrisca sobreescriure edicions alienes. Reprèn des d'un estat verificat. Si no tens accés a la font, tria `Hold` en lloc de deduir l'estat a partir del registre antic.

## Comparar decisions de recuperació

| Situació | Decisió que cal revisar | Motiu |
|---|---|---|
| **Requisit canviat, fusió denegada** | Completar o compensar el requisit | La intenció i el comportament difereixen |
| **Configuració canviada, runbook denegat** | Completar el runbook o desfer la configuració | Les instruccions operatives estan desactualitzades |
| **Un altre responsable canvia l'abast** | Tornar a `Review` | L'aprovació fixa descriu un altre text |
| **Resultat d'escriptura desconegut** | Llegir primer la destinació | El reintent depèn de l'estat observat |
| **El publicador perd l'accés** | Mantenir `Hold` i demanar administració autoritzada | L'autorització anterior no permet escriptures noves |

**Decideix segons l'estat actual i la decisió del responsable.** Completar el canvi requereix aprovacions actuals i controls viables. La compensació exigeix revisar la restauració respecte de les edicions intermèdies. Una recuperació és una altra publicació, no una excepció privilegiada al procés.

## Comprovació de finalització de la publicació

**Lliura un paquet que un revisor independent pugui conciliar.** Ha de trobar la proposta exacta revisada, les bases d'origen, les dues revisions per rol, el resultat de cada escriptura, els valors finals i les limitacions d'execució pendents. Demana-li que identifiqui el primer pas incomplet després d'una interrupció.

**Raonament esperat:** la següent acció surt de les fonts recents i del registre, no de la confiança de l'assistent anterior. Porta les referències assignades finals a les proves de recuperació, on la cerca ha de conservar la mateixa distinció d'autoritat.

## Solució de problemes i recuperació

**Versió canviada:** compara l'historial i renova la revisió. **La comprovació de la instantània passa però la wiki difereix:** torna a obtenir les fonts actuals de Confluence. **S'ha posat Done massa aviat:** torna a obrir l'element mitjançant el flux permès i registra els passos que falten.

**Recuperació:** utilitza la comparació de Page History i una restauració o edició compensatòria revisada per un responsable. Registra la versió resultant en lloc de pressuposar que la restauració reinicia la numeració. Reverteix la configuració mitjançant una PR protegida si Producte tria la reversió. Els fitxers eliminats queden fora de la garantia de reversió.

## Exercici i autoavaluació

**Interromp el procés després de publicar REQ-17** i dona a un altre publicador només el mapa i el registre.

**Raonament esperat:** consulta les fonts actuals, confirma l'aprovació fixa i reprèn només el pas pendent autoritzat. La manca de proves retorna la feina a `Review`.

## Referències principals

- **Historial i restauració:** [documentació tècnica de Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Operacions de l'API amb versions:** [pàgines de Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Controls del flux de treball:** [fluxos de treball avançats de Jira](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Seguretat de la integració:** [bones pràctiques de seguretat de MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Passos següents

**Continua amb [Recuperació amb el mapa com a punt de partida](/articles/ai-collaboration-map-first-retrieval/)** després de completar una ronda de publicació revisada.
