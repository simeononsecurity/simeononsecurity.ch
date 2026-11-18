---
title: "Claus SSH de Bitbucket Cloud: accés Git de només lectura per a agents d’IA"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "Configureu les claus SSH de Bitbucket Cloud, l’accés Git CLI, els tokens REST API, 1Password i les eines MCP per a fluxos de treball d’agents d’IA de només lectura."
genre: ["Seguretat al núvol", "Eines per a desenvolupadors", "Administració de sistemes"]
tags: ["Bitbucket Cloud", "claus SSH de Bitbucket", "claus d’accés al repositori", "claus d’accés al projecte", "claus d’accés a l’espai de treball", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "àmbits dels tokens API", "permisos dels agents", "automatització de només lectura", "claus d’amfitrió SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Flux de treball de terminal que connecta l’accés Git de Bitbucket Cloud, claus SSH d’abast limitat, 1Password, lectures REST API i eines MCP"
coverCaption: ""
---

**Un flux de treball d’agent delimitat separa les lectures del repositori, les lectures de l’API, la gestió de secrets i les escriptures remotes.** Feu servir Git mitjançant Secure Shell (SSH) per accedir al codi font, una clau d’accés de Bitbucket de només lectura per a les extraccions automatitzades, REST API per a les metadades i un servidor Model Context Protocol (MCP) per a les eines aprovades. Deseu les claus privades i els tokens API a 1Password. Exigiu aprovació humana abans d’escriure.

<!--more-->

## Punts clau

- **Només lectura per defecte:** feu servir una clau d’accés al repositori o al projecte per a l’extracció de l’agent. Cap de les dues no permet fer push.
- **Identitat personal:** feu servir una clau SSH personal per a la feina interactiva vinculada a un compte d’usuari.
- **Custòdia de secrets:** feu servir 1Password SSH Agent perquè Git sol·liciti una signatura autoritzada sense llegir la clau privada.
- **Significat de CLI:** considereu `git`, `curl` i un petit wrapper API auditat com la línia d’ordres pràctica de Bitbucket.
- **Límit de MCP:** exposeu eines de lectura d’abast reduït. Desactiveu les eines d’escriptura o poseu-les darrere d’un procés d’aprovació separat.
- **Control d’escriptura:** permeteu que l’agent inspeccioni, compari i prepari un canvi. Exigiu que una persona aprovi un push, una pull request, una fusió o un canvi de configuració.

## Abans de començar

**Requisits previs:** accés a Bitbucket Cloud, Git, un client OpenSSH, 1Password 8, 1Password CLI, una CLI amb sessió iniciada o un compte de servei aprovat, i un amfitrió MCP amb controls d’aprovació de servidors. Reserveu 45 minuts. Dificultat intermèdia.

Feu servir un repositori de prova per a la primera passada. Substituïu tots els marcadors de posició dels exemples. Les ordres següents són exemples no provats. No representen cap compte ni repositori Bitbucket actiu.

**Versions:** aquest article ofereix orientació de disseny, no un procediment fixat a versions concretes. Confirmeu les versions instal·lades de Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, l’amfitrió MCP i el servidor MCP abans de provar. Configureu 1Password SSH Agent per al sistema operatiu actual abans de fer servir `ssh-add -l`.

**Manteniu les credencials fora dels shells, els registres, les URL, els remots Git i els fitxers font.** Feu servir marcadors com ara `<workspace>`, `<repository>`, `<api-token>` i `<socket-path>`. No enganxeu una clau privada real en una transcripció de terminal.

## Trieu el límit d’accés

Bitbucket Cloud admet claus d’accés a nivell de repositori, projecte i espai de treball. L’abast canvia l’impacte d’una clau copiada. La [comparació oficial de claus d’accés](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) explica directament les diferències de permisos.

| Via d’accés | Abast | Permet escriure | Ús adequat |
|---|---|---:|---|
| **Clau d’accés al repositori** | Un repositori | No | Extracció predeterminada d’un agent |
| **Clau d’accés al projecte** | Repositoris d’un projecte | No | Tasques de només lectura en un grup reduït de repositoris |
| **Clau d’accés a l’espai de treball** | Repositoris d’un espai de treball | Sí | Automatització de servei controlada amb un pla d’escriptura separat |
| **Clau SSH personal** | Repositoris permesos a un usuari | Segueix el compte de l’usuari | Administració interactiva |
| **Token API** | Àmbits API basats en l’usuari i accés del compte | Depèn dels àmbits | Lectures REST API o una tasca temporal d’escriptura |

**Comenceu pel límit útil més petit.** Trieu una clau de repositori si n’hi ha prou amb un. Trieu una clau de projecte si diversos repositoris comparteixen projecte i és suficient l’accés de només lectura. Tracteu una clau d’espai de treball com una identitat d’escriptura, no com una opció predeterminada còmoda.

Creeu i registreu la clau més restringida mitjançant el camí corresponent dels paràmetres de Bitbucket:

1. Obriu Repository settings, Access keys i Add key per a un repositori. Enganxeu la clau pública i manteniu la clau en mode de només lectura.
2. Obriu Project settings, Access keys i Add key quan diversos repositoris necessitin una identitat de lectura limitada al projecte.
3. Feu servir una clau d’espai de treball només en un espai compartit amb un disseny d’escriptura aprovat. Els espais de treball personals no ofereixen el mateix camí a nivell d’espai.
4. Anoteu l’etiqueta de la clau, l’abast, l’empremta de la clau pública, el propietari i la data de rotació. Deseu la clau privada a 1Password.

Després del registre, feu una prova exacta de connexió de només lectura:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Resultat esperat:** una referència de commit per a `HEAD`. Exemple no provat. Un resultat correcte demostra que una identitat SSH permesa ha arribat al repositori indicat. No demostra que s’hagi seleccionat la clau registrada ni que hi hagi accés d’escriptura. Repetiu la prova després de configurar una clau per repositori.

Per a la custòdia de claus privades i el consentiment de 1Password SSH Agent, consulteu [1Password CLI i SSH Agent: claus SSH segures per a agents d’IA](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Definiu correctament «Bitbucket CLI»

L’expressió **Bitbucket CLI** sovint barreja tres interfícies diferents. Manteniu-les separades.

- **Git CLI:** `git clone` i `git fetch` mouen dades del repositori per SSH o HTTPS. `git diff` compara fitxers locals o revisions.
- **Client REST:** `curl` o un wrapper revisat crida l’API Representational State Transfer (REST) de Bitbucket Cloud. Una API és una interfície programàtica per sol·licitar dades o accions. La [referència Bitbucket Cloud REST API](https://developer.atlassian.com/cloud/bitbucket/rest/) enumera recursos de repositori, font, branca, pull request, pipeline i estat.
- **Atlassian CLI:** `acli` és la línia d’ordres oficial d’Atlassian. La seva [introducció](https://developer.atlassian.com/cloud/acli/guides/introduction/) descriu el producte, mentre que la seva [referència d’ordres](https://developer.atlassian.com/cloud/acli/reference/commands/) enumera les interfícies `admin`, `jira`, `feedback` i `rovodev`. La referència no documenta ordres de Bitbucket Cloud.

**La referència oficial d’ordres `acli` d’Atlassian no documenta ordres de Bitbucket Cloud.** No inventeu una ordre com ara `acli bitbucket clone`. Feu servir Git per a les operacions Git i REST API per a les dades de Bitbucket Cloud.

### Teamwork Graph CLI opcional

**Atlassian també publica Teamwork Graph CLI, o `twg`.** La seva [introducció](https://developer.atlassian.com/cloud/twg-cli/) i el [catàleg d’ordres](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documenten famílies d’ordres de Bitbucket. L’ordre de configuració és:

```bash
twg setup
```

L’ordre de configuració canvia l’estat d’autenticació local. Seguiu les indicacions de la versió instal·lada per configurar opcionalment un token de Bitbucket. El camí del token Bitbucket de la CLI és independent de l’OAuth d’Atlassian. Ajusteu la sintaxi exacta de les ordres a la versió instal·lada i al catàleg actual. Feu servir un perfil separat, un token restringit, habilitats instal·lades revisades i aprovació humana per a ordres que modifiquen dades.

**Resultat esperat, no provat:** el perfil aïllat rep la configuració d’autenticació de Bitbucket. Anoteu l’estat anterior del perfil abans de configurar-lo. Per revertir-ho, elimineu la credencial desada mitjançant el procediment documentat de tancament de sessió o d’eliminació de configuració de la versió instal·lada.

Si un projecte de tercers es presenta com una Bitbucket CLI, auditeu-ne el codi font, el procés de publicació, les sumes de verificació, la via d’actualització, el flux d’autenticació, els àmbits sol·licitats, les destinacions de xarxa, la gestió dels registres i les ordres d’escriptura. Un nom de binari conegut no demostra suport del proveïdor ni permisos segurs.

## Manteniu les claus SSH sota el control de 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) ofereix les claus SSH desades a 1Password a Git i als clients SSH. El client fa una sol·licitud de signatura autoritzada. La clau privada es manté dins de l’aplicació 1Password, que demana consentiment abans que un client aprovat faci servir una clau.

La [referència de 1Password CLI](https://www.1password.dev/cli/reference) té una funció diferent. Feu servir `op` per accedir de manera controlada a elements, tokens API, comptes de servei i configuració d’automatització. Feu servir SSH Agent per signar amb SSH. Eviteu exportar una clau privada a un fitxer temporal per facilitar el flux de treball d’un agent.

Comproveu l’estat local de la CLI i de l’agent amb ordres de només lectura:

```bash
op --version
ssh-add -l
```

**Resultat esperat:** una versió de 1Password CLI i una o més empremtes de claus públiques de l’agent actiu. Exemple no provat. Un resultat buit de `ssh-add -l` significa que no hi ha cap clau disponible mitjançant el socket d’agent seleccionat.

Per a una clau nova, creeu un element SSH Key Ed25519 a 1Password o importeu-ne una de generada amb un procés local de confiança. Poseu-hi una etiqueta segons l’ús, l’abast i la data de rotació. Afegiu només la clau pública a Bitbucket Cloud. La [guia Linux de claus d’accés a repositoris](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) descriu el camí dels paràmetres del repositori i el límit de només lectura.

## Verifiqueu primer la clau d’amfitrió de Bitbucket

L’autenticació SSH de l’usuari no demostra la identitat del servidor. El client ha de verificar la clau d’amfitrió de Bitbucket Cloud abans d’enviar una sol·licitud d’autenticació. La [guia d’Atlassian sobre SSH i la verificació en dos passos](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) enumera les claus d’amfitrió públiques i mostra el punt final oficial per recuperar entrades known-hosts.

Recupereu les dades públiques de la clau d’amfitrió per comparar-les:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Resultat esperat:** línies OpenSSH `known_hosts` per a `bitbucket.org`. Exemple no provat. Compareu la clau o l’empremta retornada amb una còpia independent de confiança abans de col·locar la línia a `~/.ssh/known_hosts`.

Feu servir una comprovació estricta de l’amfitrió un cop existeixi l’entrada aprovada:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**No accepteu una clau d’amfitrió canviada durant una execució d’agent.** Atureu l’execució, verifiqueu el registre actual de claus d’amfitrió de Bitbucket Cloud i reviseu l’entrada local de `known_hosts`. Una acceptació automàtica elimina un límit de seguretat basat en claus.

## Seleccioneu una clau per repositori

Un dispositiu sovint té diverses claus Bitbucket. Un agent SSH ampli ofereix diverses identitats en una connexió. Un servidor o una política amb un límit baix d’intents d’autenticació podria rebutjar la clau correcta després que fallin les anteriors.

La [guia d’Atlassian sobre diverses claus d’accés a repositoris](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) fa servir `core.sshCommand` en un fitxer de configuració Git del repositori i `includeIf` a la configuració global de Git. Seguiu el mateix patró per fer servir una clau per repositori.

Exemple portàtil amb fitxers:

```ini
# .gitconfig dins d’un únic repositori local
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

El bloc anterior és una excepció de fitxer de clau privada per a una identitat d’automatització dedicada. No configura 1Password SSH Agent. Per a 1Password SSH Agent, configureu el valor `IdentityAgent` o `SSH_AUTH_SOCK` específic de la plataforma segons la [guia de configuració de 1Password](https://www.1password.dev/ssh/get-started). Algunes configuracions OpenSSH fan servir un fitxer `.pub` com a selector d’identitat de l’agent. Confirmeu la compatibilitat de la plataforma abans de fer-ho. Una configuració basada en fitxer necessita el camí de la clau privada corresponent. No passeu mai un fitxer `.pub` a una ordre que esperi material de clau privada ni exporteu una clau privada personal.

Feu servir una configuració explícita del repositori quan un clon local necessiti una clau concreta. Feu servir `includeIf` quan un directori contingui diversos clons amb el mateix límit d’accés. La [guia de claus múltiples](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) mostra tots dos paràmetres al flux de Bitbucket.

Cloneu amb Git per SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Resultat esperat:** Git crea `<local-directory>` i obté el repositori mitjançant `bitbucket.org`. Exemple no provat. Una clau d’accés al repositori només permet clonar i fer pull.

## Feu servir tokens API per a lectures REST limitades

Feu servir SSH per al transport Git. Feu servir REST API per a metadades o operacions fora del transport Git. La [guia de permisos dels tokens API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) enumera àmbits del repositori com Read, Write, Admin i Delete. Repository Read correspon a `read:repository:bitbucket` i no inclou accés a pull requests.

Per a l’automatització de lectura, preferiu un token d’accés de repositori o projecte Bitbucket si la destinació admet el punt final necessari. Un token API d’usuari conserva l’abast més ampli del compte. Feu servir un token d’espai de treball només quan el registre de la tasca especifiqui aquest límit més ampli. Consulteu la [guia de tokens d’accés de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) abans de triar-ne el tipus.

Per a una ruta de lectura d’agent, comenceu amb `read:repository:bitbucket`. Afegiu `read:pullrequest:bitbucket` només quan l’agent necessiti dades de pull request. Afegiu àmbits d’espai de treball o de pipeline només si el registre de la tasca especifica el punt final i el resultat. Els àmbits d’escriptura i d’administració necessiten una via d’aprovació separada.

Creeu cada token API per a un sol propòsit, definiu-ne la data de caducitat, anoteu-la al registre de rotació i substituïu el token abans que caduqui. La [guia d’Atlassian per crear tokens API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) requereix un nom, una data de caducitat, la selecció de l’aplicació i els àmbits. El token només es mostra una vegada després de crear-lo.

Deseu el valor a 1Password o en un secret d’execució gestionat. No el poseu en una URL remota. Envieu un token bearer mitjançant una variable d’entorn només al procés que necessiti fer una lectura:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Manteniu `/path/to/agent.env` fora del repositori. Deseu-hi una referència com `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` resol la referència i exposa el valor al procés fill curl durant la vida del subprocés. Això no impedeix que el procés fill llegeixi el valor de la variable d’entorn o l’escrigui en un registre. No substituïu el marcador de posició per un token literal.

**Resultat esperat:** metadades JSON del repositori seleccionat. Exemple no provat. El marcador de posició no s’ha de convertir mai en un token real en un fitxer confirmat o un registre.

Per a automatitzacions més llargues, deixeu que 1Password injecti un secret a l’entorn del procés mitjançant el flux CLI o de compte de servei admès. Ajusteu la durada del token a la tasca. Revoqueu-lo si la tasca s’acaba abans d’hora o canvia el propietari de l’amfitrió.

## Doneu a MCP una petita superfície de lectura

Feu servir l’[especificació MCP actual](https://modelcontextprotocol.io/specification/2026-07-28) i les seves [regles d’autorització](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) quan reviseu un servidor nou. Els servidors HTTP necessiten comprovacions de l’audiència del token i una gestió clara de les respostes 401 i 403.

L’amfitrió MCP obté el consentiment de l’usuari. El client manté una connexió amb un servidor. El servidor exposa eines, recursos o prompts. Tracteu cada servidor com a codi no fiable fins que n’hàgiu revisat el codi font, el transport, el compte i els permisos.

L’URL d’especificació 2025-06-18 del paràgraf següent és una versió històrica. Feu servir l’especificació actual 2026-07-28 per a les noves revisions.

L’[especificació MCP](https://modelcontextprotocol.io/specification/2025-06-18) defineix la comunicació entre un amfitrió MCP, un client i un servidor. Un servidor exposa eines, recursos o prompts mitjançant el protocol. MCP estandarditza el format de connexió. L’amfitrió, la implementació del servidor, el compte, l’àmbit del token i la política d’aprovació encara determinen què pot assolir una crida.

Feu servir un servidor MCP com a adaptador restringit sobre Git i l’API REST de Bitbucket Cloud.

Protegiu l’adaptador contra el traspàs de tokens, la falsificació de sol·licituds del servidor (SSRF) i el comportament de delegat confús. SSRF permet que un servidor enviï sol·licituds a destinacions no previstes. El comportament de delegat confús es produeix quan un servidor fa servir privilegis més amplis en nom de qui el crida. Protegiu també contra servidors locals maliciosos, redireccions OAuth insegures i respostes de dades font excessivament grans. Fixeu els orígens permesos de Bitbucket i els identificadors de repositori. Executeu els servidors locals en una sandbox amb un usuari del sistema operatiu dedicat. Redacteu els secrets dels resultats de les eines i dels registres.

Aquesta secció descriu un disseny, no una configuració MCP provada. No fixa cap client, servidor, transport, versió ni fixture. Valideu un servidor de només lectura en un perfil de prova separat abans de connectar un agent a un repositori de producció.

Exemples d’eines de lectura:

| Eina | Resultat delimitat |
|---|---|
| **`get_repository_metadata`** | Retorna metadades d’un repositori |
| **`read_source_file`** | Llegeix un camí en una revisió |
| **`list_branches`** | Llista les branques d’un repositori |
| **`get_pull_request`** | Retorna una pull request quan el token té abast de lectura de pull requests |
| **`get_build_status`** | Retorna dades d’estat d’un commit |

Aquests noms descriuen un disseny. No són noms d’ordres d’Atlassian. Impediu que el servidor accepti URL arbitràries, ordres shell arbitràries, tokens sense processar, sol·licituds d’exportació de claus privades o identificadors de repositori sense restriccions.

Definiu els permisos en quatre capes:

1. **Bitbucket Cloud:** clau de lectura de repositori o projecte per a Git, més els àmbits mínims dels tokens API per a lectures REST.
2. **1Password:** una caixa forta o un compte de servei per a la tasca, sense cap via d’exportació de claus privades.
3. **Servidor MCP:** llista permesa d’eines de lectura, punts finals fixos de Bitbucket Cloud, validació d’entrades, límits de temps i registres redactats.
4. **Amfitrió MCP:** aprovació de l’usuari per al servidor i cada acció amb capacitat d’escriptura, amb les eines d’escriptura desactivades al perfil predeterminat.

*Una llista d’eines MCP demostra que s’han descobert. No demostra l’autorització, l’abast correcte, el tractament segur de les entrades ni un resultat correcte.*

## Estructureu el flux de treball de l’agent

Feu explícit el flux de treball. Cada etapa produeix evidència per a la següent.

| Etapa | Acció de l’agent | Permís | Control humà |
|---|---|---|---|
| **Preparar** | Llegir la configuració, el registre de clau d’amfitrió, l’etiqueta de clau, l’abast del token i la caducitat | Lectura local | Aprovar el registre de configuració |
| **Inspeccionar** | Clonar o fer fetch mitjançant Git per SSH i consultar metadades REST | Lectura del repositori i de l’API | Cap després de configurar |
| **Analitzar** | Llegir fitxers, branques, pull requests i estat de build amb eines aprovades | Eines MCP de només lectura | Cap per a lectures delimitades |
| **Preparar el canvi** | Produir un pedaç, un pla de branca o un esborrany de pull request en un espai local | Només escriptura local | Revisar el diff i la destinació |
| **Aprovar l’escriptura** | Presentar l’acció remota exacta, l’abast i el pla de reversió | Encara cap escriptura remota | Aprovació humana |
| **Executar l’escriptura** | Fer push d’una branca, crear una pull request o cridar un punt final d’escriptura | Identitat d’escriptura de curta durada | Confirmar cada acció |
| **Verificar** | Llegir el commit, la pull request o l’estat resultant | De nou en mode de només lectura | Confirmar el resultat esperat |

El perfil predeterminat de l’agent s’hauria d’aturar després d’**Analitzar** o **Preparar el canvi**. Un perfil d’escriptura separat hauria d’utilitzar un altre token o clau, una caducitat curta, una destinació fixa i una sol·licitud d’aprovació. Una clau d’accés al repositori no permet fer el pas d’escriptura, cosa que crea un límit tècnic útil.

## Reversió i eliminació

Comenceu la reversió eliminant l’accés i després netegeu la configuració local:

1. Elimineu la clau d’accés al repositori, projecte o espai de treball de la pàgina de configuració Bitbucket corresponent.
2. Revoqueu el token API del repositori, projecte, espai de treball o usuari a la pàgina de seguretat Bitbucket corresponent.
3. Elimineu la credencial desada de Teamwork Graph mitjançant el [procediment d’autenticació documentat](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) per a la versió de CLI instal·lada. Conserveu la credencial anterior només al gestor de secrets aprovat. Confirmeu que el perfil aïllat ja no mostra la credencial de prova.
4. Un cop acabada la prova, elimineu el fitxer `.gitconfig` del repositori i la seva entrada `includeIf`. Manteniu intacta la configuració Git no relacionada.
5. Elimineu només la línia de clau d’amfitrió Bitbucket verificada que heu afegit per a la prova. Manteniu les altres claus d’amfitrió aprovades.
6. Elimineu el fitxer extern `agent.env` i la sortida temporal. Elimineu l’entrada del servidor MCP de la configuració de l’amfitrió i reinicieu-lo.

Registreu cada eliminació, l’operador i l’hora. Roteu una clau o un token si un valor apareix en un registre, registre de procés o transcripció inesperats.

## Bucle de lectura remota amb actualitzacions locals de referències

Feu servir un bucle petit per inspeccionar regularment un repositori:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` és la referència actual del repositori. Un resultat correcte demostra que una identitat SSH permesa ha arribat al repositori indicat. No demostra quina clau s’ha seleccionat ni si existeix accés push.

**Resultat esperat:** resultat de fetch, estat de branca i una línia de commit. Exemple no provat. `fetch` no escriu al remot, però actualitza les referències locals i `FETCH_HEAD`. El bucle no fa push ni canvia de branca.

El servidor MCP hauria d’exposar el mateix límit de lectura mitjançant operacions amb nom. Un wrapper shell local o una eina MCP hauria de rebutjar un verb d’escriptura abans d’enviar una sol·licitud. Registreu el nom de l’eina, el marcador del repositori, la revisió, la classe del resultat i la durada. Redacteu tokens, cookies, camins privats i contingut dels fitxers, tret que la tasca necessiti explícitament un fitxer.

## Resolució de problemes

### `Permission denied (publickey)`

Comproveu el socket de l’agent actiu, la clau pública seleccionada, l’entrada de clau d’accés al repositori i `IdentitiesOnly`. Una clau de repositori ha d’existir al repositori o projecte de destinació. Una clau personal necessita permís del compte. Una clau d’espai de treball té un límit d’escriptura diferent.

### S’ofereix la clau de repositori equivocada

Feu servir una clau per repositori amb `core.sshCommand`, o agrupeu els clons en un directori controlat per `includeIf`. Llisteu les claus de l’agent amb `ssh-add -l`. Si hi ha moltes claus 1Password, feu servir un selector d’identitat explícit o un marcador SSH de 1Password. La [guia 1Password Agent](https://www.1password.dev/ssh/agent) documenta les consideracions sobre el nombre de claus i els marcadors.

### SSH informa d’un canvi de clau d’amfitrió

Atureu l’agent. No elimineu `known_hosts` com a primera resposta. Compareu el registre actual de claus d’amfitrió de Bitbucket Cloud amb l’entrada local mitjançant un canal independent. Elimineu o substituïu una entrada només després de superar la comparació.

### L’API retorna `401` o `403`

Comproveu la caducitat i el tipus del token, l’abast del punt final i el límit del compte o de l’espai de treball. Un àmbit de lectura del repositori no inclou pull requests. Un punt final d’escriptura necessita un àmbit d’escriptura i un perfil d’escriptura aprovat. No amplieu els àmbits fins que identifiqueu el punt final que ha fallat.

### L’API retorna dades del repositori però no pull requests

Afegiu l’àmbit mínim de lectura de pull requests a un token nou o rotat. No reutilitzeu un token d’usuari ampli per a un servidor MCP de només lectura.

### El servidor MCP llista eines però falla una crida

Separeu el registre del servidor, la connexió, la descoberta d’eines, l’execució i la verificació del resultat. Inspeccioneu el registre del servidor sense exposar el token. Verifiqueu el punt final i la forma de l’entrada. Torneu-ho a provar una vegada després de comprovar la connectivitat. Marqueu l’operació com a incompleta si falla el segon intent.

### Una CLI Bitbucket de tercers demana accés ampli

Atureu la instal·lació. Compareu l’accés demanat amb el registre de la tasca. Reviseu el codi font, les signatures o sumes de verificació de les publicacions, les destinacions de xarxa, l’emmagatzematge de secrets i el comportament d’escriptura. La referència oficial d’ordres Atlassian CLI no demostra compatibilitat amb un binari Bitbucket de tercers.

## Passos següents

Creeu un registre breu d’accés amb l’abast del repositori o projecte, l’etiqueta de la clau, la data de verificació de la clau d’amfitrió, els àmbits API, la caducitat del token, el propietari de 1Password, la llista permesa d’eines MCP, la política de registres i la persona que aprova les escriptures.

Feu un clon de només lectura, una lectura de metadades REST i una lectura d’una eina MCP amb marcadors de posició a la transcripció. Compareu els resultats. Manteniu el perfil de l’agent en només lectura fins que es revisin el registre i els registres.

Quan arribi una tasca d’escriptura, prepareu primer un diff local. Presenteu la branca de destinació, els camins modificats, el mètode API sol·licitat, l’àmbit del token i el pas de reversió. Feu servir una identitat d’escriptura separada i de curta durada només després que una persona aprovi l’acció exacta.
