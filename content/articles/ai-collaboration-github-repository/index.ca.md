---
title: "Col·laboració d'IA a GitHub: límits del repositori i de la revisió"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Crea un mapa de fonts basat en GitHub, assigna propietaris de fitxers i estableix un límit de publicació protegit per a contribucions d'IA revisades."
genre: ["Intel·ligència artificial", "Col·laboració d'equips", "Enginyeria de programari"]
tags: ["curs de col·laboració d'IA", "repositori de GitHub", "protecció de branques", "CODEOWNERS", "mapa de fonts", "revisió de pull requests", "controls de publicació"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Il·lustració de professionals que revisen treball compartit en un espai de ciberseguretat"
coverCaption: ""
---

[Torna al curs de col·laboració d'IA](/ai-collaboration-course-start/)

**El mantenidor construeix el límit de publicació basat en GitHub** després d'aprovar l'acta. Els requisits, la configuració, la política i els procediments viuen en un repositori d'un sol ús. Els col·laboradors proposen mitjançant Issues i pull requests. Tu estableixes on viuen els fets aprovats i bloqueges els canvis sense revisió abans d'adjuntar agents.

## Punts clau

- **`main` protegit** és el límit de publicació.
- **Les Issues** recullen feina proposada sense aprovar polítiques.
- **CODEOWNERS** assigna revisors de fitxers elegibles.
- **Usuaris separats** demostren els controls de revisió i denegació.

## Abans de començar

**Requisits previs:** la [base del pilot](/articles/ai-collaboration-pilot-foundation/), el laboratori extret, un administrador del repositori i revisors separats de producte i operacions. **Temps estimat:** 60 minuts. **Dificultat:** moderada.

**Límit del pla:** GitHub documenta branques protegides per a repositoris públics a Free i repositoris privats a Pro, Team o Enterprise. Usa repositoris públics només per a contingut sintètic. Verifica la visibilitat i el pla contra la referència de branques protegides abans de confiar en l'aplicació.

**Resultat:** acabes amb una branca de publicació protegida, propietaris de fitxers, un mapa de fonts i una prova de denegació registrada com a evidència.

## Crear el repositori

1. **Crea `export-service-lab`** amb un README i la branca predeterminada **`main`**.
2. **Copia el laboratori extret** a l'arrel del repositori i conserva **`check.py`**, **`test_check.py`** i **`baseline/`**. Copia els fitxers de registre de referència a l'arrel com a registres inicials.
3. **Crea `docs/project-map.md`** amb el registre de la base. Afegeix **`docs/policy.md`** amb el POL-01 aprovat.
4. **Crea `docs/decisions/DEC-12.md`** amb l'aprovació de l'acta, els rols, la decisió de referència i l'estat.
5. **Fes el commit d'arrencada** com a administrador. Registra aquesta excepció inicial. Activa la protecció abans de les contribucions posteriors.

**Ruta d'arrencada local per a Git Bash, Terminal de macOS o un shell de Linux:** inicia sessió a GitHub des d'un navegador, obre el repositori nou, selecciona **Code** i copia'n l'URL HTTPS de clonació. En un directori de treball d'un sol ús, executa les ordres següents. Substitueix les dues rutes de marcador per l'URL i la ruta del ZIP del laboratori descarregat. No enganxis cap token a l'URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

L'ordre clone ha de donar nom al directori del repositori. Si `unzip` no està disponible, extreu el ZIP amb el gestor de fitxers i copia'n el contingut en aquest checkout, deixant intacte el README. `git status --short` ha de mostrar els registres copiats, el verificador, les proves i `baseline/` com a fitxers nous. Desa `docs/project-map.md`, `docs/policy.md` i `docs/decisions/DEC-12.md` del paquet de la base amb un editor de text. Després executa:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git ha de mostrar un ID de commit nou i després un push correcte a `main`. L'estat curt final ha d'estar buit. Obre el repositori de GitHub en una vista nova del navegador i confirma que els fitxers i l'ID del commit apareixen a `main`. Desa l'URL del commit com a evidència d'arrencada. Si Git demana la identitat de l'autor, segueix el pont de configuració del centre del curs. Si falla l'autenticació, usa el flux de credencials compatible amb GitHub i repeteix el mateix push. Si la branca o el remot són incorrectes, atura't i inspecciona `git branch --show-current` i `git remote -v` abans d'escriure de nou. Si el push és rebutjat perquè la protecció ja estava activa, obre una branca de proposta i una PR en lloc d'evitar la regla. La ruta només amb navegador continua disponible mitjançant un mantenidor.

| Registre | Ubicació | Propietari |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Propietari de política |
| **REQ-17** | `requirement.json` | Propietari de producte |
| **RUN-04** | `runbook.md` | Propietari d'operacions |
| **Comportament** | `config.json` | Mantenidor |
| **Decisions** | `docs/decisions/` | Líder del projecte |

**El mapa enllaça ubicacions en lloc de copiar valors.** Mantén el README centrat en la configuració i el mapa. Repetir requisits de retenció crea divergències fins i tot dins d'un sol repositori.

## Assignar propietaris de fitxers

**Genera `.github/CODEOWNERS`** localment amb identificadors reals de l'entorn aïllat. Introdueix els identificadors sense el **`@`** inicial. Mantén les identitats dels comptes al teu laboratori privat, no a l'evidència pública de l'exercici.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Els propietaris necessiten accés d'escriptura** perquè GitHub els reconegui. Inspecciona el fitxer CODEOWNERS al navegador per detectar errors. Protegeix els fitxers de propietaris i les definicions de flux de treball juntament amb el contingut normal.

**Diversos noms en una línia no requereixen l'aprovació de tothom.** GitHub accepta l'aprovació d'un propietari elegible per a la ruta corresponent. Usa propietaris designats diferents per a les rutes de requisits i procediments. El pilot també requereix declaracions de producte i operacions vinculades a la proposta final.

## Protegir la publicació

1. **Obre Settings, Branches** i afegeix una regla de protecció de branques per a **`main`**. Usa la ruta de protecció de branques de manera coherent en lloc de barrejar-la amb rulesets durant aquest exercici.
2. **Exigeix una pull request**, dues revisions aprovadores i la revisió dels propietaris del codi.
3. **Descarta les aprovacions obsoletes** després de nous commits i exigeix resoldre les converses.
4. **Activa No permetre ometre les configuracions anteriors.** Mantén desactivades les pujades forçades i l'eliminació.
5. **Afegeix la comprovació de consistència** després de la seva primera execució al mòdul següent. Exigeix que les branques estiguin actualitzades abans de fusionar-les.

**Dues aprovacions imposen una quantitat, no pertinença a rols empresarials.** CODEOWNERS afegeix cobertura de propietaris per ruta. El mantenidor també comprova les dues declaracions de rols. Registra aquest control procedimental explícitament en lloc de descriure'l com a aplicació automatitzada de dos rols.

**Els administradors continuen gestionant la configuració.** Captura la regla abans i després de les proves. No donis accés d'administrador a un agent ni usis un token privilegiat per demostrar la denegació del col·laborador.

## Verificar el límit

| Intent | Resultat esperat |
|---|---|
| **El col·laborador envia una branca** | Proposta permesa |
| **El col·laborador publica directament** | Publicació protegida denegada |
| **Un revisor aprova** | La fusió queda bloquejada pel llindar de revisió |
| **Un commit nou segueix la revisió** | Cal una aprovació nova |
| **Un fitxer sensible no té cobertura de propietari** | Reparar abans de publicar |

**Usa la sessió de navegador del col·laborador per inspeccionar la ruta.** L'editor web de GitHub no edita una branca **`main`** protegida. Un avís per crear una branca mostra la ruta compatible amb el navegador. No demostra que el servidor hagi rebutjat un push directe. Per obtenir evidència de denegació de plataforma, fes que un col·laborador amb accés Git local aprovat intenti un push directe i inofensiu a **`main`** protegida i conserva la resposta del servidor. Marca aquesta prova de denegació com a Bloquejada quan no hi hagi accés local.

**Llegeix `main` després de la denegació** i confirma que la revisió no ha canviat. Registra el rol de l'actor, l'acció intentada, el resultat i la revisió d'origen. Un assistent que promet no publicar aporta evidència de comportament, no una prova de permisos de plataforma.

**Usa el clon local autenticat del mateix col·laborador per a la prova de push directe.** Un token del mantenidor provaria la identitat equivocada. Aquesta resposta il·lustrativa mostra el tipus d'evidència del servidor que cal conservar. El text exacte varia segons les regles del repositori.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Si l'autenticació Git local no està disponible, marca la denegació del servidor com a Bloquejada.** Conserva l'avís de branca del navegador com a evidència de ruta i demana al mantenidor que organitzi una prova separada amb un col·laborador. No puntuis l'avís de ruta com un push directe rebutjat.

## Crear un mapa de fonts útil

**Un mapa de fonts és un document d'encaminament**, no un segon document de requisits. Algú que arriba des del xat ha de trobar la intenció actual, el comportament implementat i les instruccions operatives sense triar entre resums que competeixen.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**No posis el valor actual de retenció a cada entrada del mapa.** Un mapa que conté “set dies” es converteix en un altre valor per sincronitzar després de PROP-042. Conserva identificadors i ubicacions estables al mapa, i llegeix el valor del registre autoritzat.

**Protegeix els canvis del mapa com a canvis d'encaminament.** Redirigir REQ-17 a un fitxer d'esborrany canvia la selecció de fonts encara que el requisit aprovat continuï intacte. Revisa la destinació, el propietari i l'abast d'autoritat cada vegada que canviï el mapa.

## Separar la base i la proposta

**L'arrel del repositori conté els registres actius del laboratori.** El directori **`baseline/`** descarregat és un recurs didàctic. No és automàticament la base protegida per a cada PR posterior. Quan el treball revisat arriba a **`main`**, els registres protegits de l'arrel defineixen la base de la proposta següent.

| Ubicació | Propòsit | Editar durant PROP-042? |
|---|---|---|
| **Requisit/configuració/procediment de l'arrel** | Registres actius proposats a la branca | Sí, mitjançant canvis revisats |
| **`baseline/`** | Recurs original de l'exercici fora de línia | No |
| **Worktree fiable separat** | Registres protegits capturats de l'arrel | No |
| **`context.json`** | Evidència dels bytes de la base capturada | Regenera després de reconciliar |

**Mantén separats els canvis de control i els de retenció.** Primer inicia el verificador i les regles de revisió. Després proposa el canvi de set a trenta dies. Combinar una reescriptura de política, una reescriptura de flux i un canvi de valor dificulta distingir controls reparats de controls eludits.

## Revisar el canvi complet

**Obre els fitxers modificats abans d'acceptar una descripció de PR.** La descripció explica la intenció de l'autor. El diff revela el canvi enviat. Per a PROP-042, inspecciona la revisió del requisit, les exclusions d'abast, la configuració, el procediment, la base de la proposta i l'evidència del manifest.

1. **Revisió de producte:** confirma la intenció de trenta dies i les exclusions sense canvis.
2. **Revisió d'operacions:** confirma que el procediment coincideix amb la configuració proposada i conserva la limitació d'execució.
3. **Revisió del mantenidor:** inspecciona JSON, captura d'origen, resultats de comprovació i canvis no relacionats.
4. **Revisió de control:** inspecciona per separat qualsevol canvi de mapa, política, CODEOWNERS o flux de treball.

**Una comprovació correcta no explica una eliminació no relacionada.** Si la branca elimina el document de política mentre canvia la retenció, demana una proposta separada o una revisió específica del propietari. Limitar l'abast manté comprensible l'objecte de revisió.

## Diagnosticar una prova de denegació

**Usa una acció intentada per cada fila d'evidència.** “El col·laborador ha fallat” és ambigu. L'usuari podria no tenir accés normal d'escriptura, trobar una limitació del navegador o topar amb la regla de branca prevista. Cada observació estableix un límit diferent.

| Observació | Interpretació | Seguiment |
|---|---|---|
| **No pot crear cap branca** | Falta accés de contribució | Usa una ruta aprovada d'Issue o fork |
| **Crea una branca, no pot publicar a main** | La ruta de publicació provada està restringida | Captura la revisió intacta de main |
| **La fusió es bloqueja amb una revisió** | El recompte de revisions s'aplica a la PR provada | Afegeix evidència específica del rol |
| **L'administrador publica malgrat la regla** | La identitat provada evita el límit | Inspecciona la configuració d'omissió i els permisos |

**Registra el rol i l'acció sense exposar dades del compte** a l'evidència compartida del curs. Conserva els registres natius de l'actor disponibles en privat per al revisor. Captura junts la configuració de la regla, l'operació intentada, la denegació i la revisió protegida resultant.

## Comprovació de finalització del repositori

**Entrega un repositori que un altre col·laborador pugui recórrer de manera independent.** El README apunta al mapa, el mapa resol els registres autoritzats, la cobertura de propietaris inclou rutes sensibles i la protecció s'aplica a **`main`**. Conserva una proposta permesa i un intent de publicació denegat.

**No afirmis que hi ha aplicació basant-te només en la configuració.** La configuració estableix el comportament previst. L'intent de l'entorn aïllat estableix el comportament observat per a un rol i una ruta concrets. Porta totes dues proves a la lliçó d'agents i Actions.

## Resolució de problemes i reversió

**Falta una sol·licitud de propietari:** confirma l'accés d'escriptura i la cobertura de rutes de la branca base. **Falta protecció:** verifica el pla i la visibilitat. **La fusió continua habilitada:** inspecciona l'objectiu de la regla, la configuració d'omissió i el recompte de revisions.

**Reversió:** tanca les propostes sense fusionar i desactiva l'automatització del laboratori. Reverteix el contingut fusionat mitjançant una altra PR revisada. Conserva l'evidència abans d'eliminar el repositori d'un sol ús. No debilitis la protecció per acabar una prova fallida.

## Exercici i autoavaluació

**Proposa una edició de `docs/policy.md`** com a col·laborador. Decideix si l'aprovació del mantenidor per si sola estableix l'aprovació del propietari de la política.

**Raonament esperat:** el recompte de revisions per si sol no estableix autoritat. La ruta necessita cobertura del propietari de política i revisió del rol actual. Enumera els requisits específics del rol que no estiguin aplicats com a controls procedimentals.

## Referències principals

- **Controls de pla i revisió:** [Branques protegides](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Elegibilitat dels propietaris:** [Propietaris del codi](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contribució des del navegador:** [Editar fitxers](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Passos següents

**Continua amb [Adaptadors d'agents i Actions](/articles/ai-collaboration-github-agents-actions/)** per connectar l'evidència de fonts amb comprovacions executables.
