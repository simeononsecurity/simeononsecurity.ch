---
title: "1Password SSH Agent and CLI: Accés de només lectura per a agents d'IA"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Dissenyar un flux de treball SSH de només lectura amb 1Password CLI, l'Agent SSH i MCP. Utilitzar comandes sintètiques, permisos restringits i aprovació humana abans de les proves en directe."
genre: ["Administració de sistemes", "Seguretat en la núvol", "Automatització"]
tags: ["1Password CLI", "Claus SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "Administració d'agents", "Administració de sistemes", "Bitbucket Cloud", "Git per SSH", "Referències de secrets", "Comptes de servei", "Principi de mínim privilegi", "Autenticació amb clau pública", "Gestió de secrets", "Seguretat de la línia de comandes", "Seguretat de l'automatització"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagrama abstracte d'un agent que utilitza una referència de secret, un agent SSH i eines MCP sense mostrar claus privades."
coverCaption: ""
---

**Un agent de línia d'ordres necessita un accés útil, no una còpia de cada credencial.** Aquesta guia presenta un disseny acotat per a 1Password CLI, l'Agent SSH de 1Password, l'accés a Git de Bitbucket i el Model Context Protocol (MCP). El primer flux de treball utilitza noms sintètics, accions només de lectura i aprovació humana a la frontera SSH.

<!--more-->

La distinció clau és senzilla. **L'SSH interactiu utilitza el consentiment a través de l'Agent SSH de 1Password. L'automatització no atesa necessita una identitat separada, un accés estret i un cicle de vida de clau diferent.** No considereu una connexió MCP com a permís per executar cap dels dos fluxos de treball.

## Punts clau

- **Protecció de la clau privada:** L'Agent SSH de 1Password realitza l'autenticació SSH mantenint les claus privades dins de l'aplicació 1Password.
- **Gestió de la clau pública:** Publiqueu només una clau pública a Bitbucket o a un compte remot. Mantingueu la meitat privada en un element de Clau SSH.
- **Consentiment interactiu:** Una persona aprova un client o una sessió de terminal abans que l'Agent SSH utilitzi una clau.
- **Separació no atesa:** Una tasca programada necessita un compte de servei dedicat i un abast de bóveda estret. Una aprovació de l'Agent SSH interactiu no satisfà aquesta necessitat.
- **Límits de MCP:** MCP connecta un agent amb eines i recursos. El client, el servidor, el sistema operatiu i la política de 1Password continuen controlant l'accés.

## Abans de començar

**Prerequisits:** Installeu 1Password 8 i 1Password CLI 2.20.0 o posterior. Inicieu sessió a través d'un compte de 1Password compatible. Utilitzeu un client OpenSSH. Creeu un repositori de Bitbucket de prova o un altre objectiu no de producció. Mantingueu disponible un segon camí administratiu per a la reversió.

**Temps:** De 30 a 45 minuts per a una revisió del disseny i una demostració sintètica.

**Dificultat:** Intermedi. Necessiteu coneixements bàsics de Git, SSH, shell i control d'accés.

Aquesta guia cobreix el disseny i la planificació. L'article enllaçat de Bitbucket cobreix els límits d'accés específics de Bitbucket. Aquesta guia no prova un compte en directe, no crea una clau real, no es connecta a un host real ni registra un servidor MCP real. Tots els identificadors següents són sintètics. **Substitueix els marcadors de posició només dins del vostre entorn controlat.**

**Postura de versió:** Utilitzeu 1Password 8 i [1Password CLI 2.20.0 o posterior](https://www.1password.dev/ssh/manage-keys) per a aquest flux de treball. [1Password CLI 1 està obsolet](https://www.1password.dev/cli/upgrade/). [1Password 7 es retira a principis de 2027](https://support.1password.com/add-account/). La generació, la importació i el compartiment de claus SSH requereixen 1Password 8. Confirmeu les versions de Git, OpenSSH, host MCP i servidor MCP instal·lades abans de provar. Els exemples següents continuen sense provar.

Un **cofre** és una col·lecció protegida d'elements de 1Password. **OpenSSH** és el programari de client i servidor SSH utilitzat per molts sistemes operatius. **MCP**, o Model Context Protocol, connecta un agent amb eines o recursos aprovats.

## Per què mantenir les claus privades sense llegir

Un parell de claus SSH té una clau pública i una clau privada. Un servei o servidor Git remot emmagatzema la clau pública. El client demostra la possessió de la clau privada durant l'autenticació. La clau privada no necessita viatjar fins al servei remot.

L'[Agent SSH de 1Password](https://www.1password.dev/ssh/agent) estén aquest model. La seva documentació indica que els clients SSH i Git s'autentiquen a través de l'agent mentre la clau privada es manté a la aplicació de 1Password. El client rep un resultat de signatura, no un fitxer de clau privada.

Aquesta frontera redueix diverses vies d'exposició:

- **Control de versions:** Una clau privada no entra en un repositori o una sol·licitud d'integració (pull request).
- **Historial de la consola:** El valor d'una clau privada no apareix en un argument de comanda.
- **Fitxers temporals:** Un script no necessita escriure una clau privada a `~/.ssh/`.
- **Context de l'agent:** Un model de llenguatge gran (LLM) no necessita el text de la clau privada per sol·licitar una operació SSH.
- **Reutilització accidental:** Una clau copiada no es manté en un espai de treball antic després que finalitzi una tasca.

La frontera no fa que SSH sigui inofensiu. Un procés amb permís per utilitzar el socket de l'agent podria realitzar accions com a la clau aprovada. La verificació de la clau de l'amfitrió, els límits de la compte remota, els permisos del repositori, la política de comandes i l'aïllament de processos encara són importants.

*La frontera de la clau privada protegeix el material de la clau. La frontera no aprova una comanda remota ni demostra que l'amfitrió objectiu és de confiança.*

## Consentiment SSH interactiu

Configureu un cofre dedicat per a les claus de l'agent. Utilitzeu el fitxer de configuració de l'Agent SSH per seleccionar el conjunt de claus més petit i una clau específica per a l'amfitrió. No exposeu totes les claus elegibles de tots els cofres integrats a un procés d'automatització.

El [model de seguretat de l'Agent SSH de 1Password](https://www.1password.dev/ssh/agent/security) vincula l'aprovació a una clau i a un procés sol·licitant. El prompt identifica el procés i la clau. La persona aleshores aprova la sol·licitud mitjançant el mètode d'autenticació configurat.

1Password documenta diversos àmbits d'aprovació. L'aprovació per clau i per aplicació és la configuració per defecte. Un àmbit de sessió de terminal restringeix l'aprovació a una pestanya o sessió. L'aprovació per sol·licitud demana de nou per a cada sol·licitud. Existeix una opció d'aprovació per a tots els processos, però aquesta opció atorga a tots els processos sota l'usuari actual del sistema operatiu accés per a la sessió.

**Utilitzeu l'abast d'aprovació més estret adequat per a la tasca.** Un agent d'administració de sistemes s'ha d'executar en un terminal dedicat o en una caixa de sorra (sandbox). No aprovigueu tots els processos quan n'hi hagi prou amb una única sessió de terminal.

La sessió d'aprovació no és una concessió permanent. 1Password registra l'autorització durant el període configurat o fins que l'aplicació es bloquegi o es tanqui. Quan l'aplicació està bloquejada, l'agent no reté les claus privades per a un ús posterior. El procés de l'Agent SSH continua en segon pla quan l'ajust compatible està habilitat mentre 1Password està tancat, però una nova sol·licitud de signatura requereix que 1Password estigui desbloquejat.

La [guia de configuració SSH de 1Password](https://www.1password.dev/ssh/get-started) mostra el flux general: generar o importar una clau, publicar la clau pública, habilitar l'Agent SSH, configurar el client SSH, executar una comanda SSH o Git i aprovar la sol·licitud. La ruta exacta del socket varia segons el sistema operatiu. Utilitzeu les instruccions de la plataforma actual en lloc de copiar una ruta d'una altra màquina.

L'aplicació 1Password ha d'estar desbloquejada abans que una nova sol·licitud de signatura tingui èxit. El procés de l'agent pot continuar en segon pla mentre l'aplicació està tancada. Una aplicació bloquejada no allibera el material de la clau privada per a la signatura.

## Claus públiques i Bitbucket

La [guia de gestió de claus de 1Password](https://www.1password.dev/ssh/manage-keys) documenta els elements de clau SSH, la generació de claus, la importació de claus, les claus públiques, les empremtes digitals i les claus privades. L'exemple de CLI utilitza `op item create --category ssh` per crear un element de clau SSH. 1Password CLI genera una clau Ed25519 per defecte per a aquest exemple i redacta la clau privada a la seva sortida.

Bitbucket Cloud utilitza el flux de treball habitual de Git i OpenSSH des de la línia d'ordres. La seva [guia de línia d'ordres](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) descriu les operacions de Git des d'un repositori local. La seva [guia de configuració SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) llista les formes remotes SSH i els formats de clau pública admesos.

**Tracteу Bitbucket com a consumidor de claus públiques.** Registreу la clau pública o l'empremta digital a través de la configuració aprovada de la compte o el repositori de Bitbucket. Mantingueу la clau privada a 1Password. El client Git demana a l'Agent SSH que signi. El client no llegeix un fitxer de clau privada.

Per a l'abast de la clau d'accés de Bitbucket, la ruta de registre i la prova de Git només lectura, vegeu [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

La documentació de Bitbucket anomena això un flux de treball de Git CLI. Aquest article no assumeix un servidor MCP de Bitbucket separat ni un producte anomenat Bitbucket CLI. Una CLI específica de Bitbucket necessita la seva pròpia documentació actual i la seva pròpia revisió de permisos.

## El límit entre l'Agent i MCP

Utilitzeu l'especificació actual de [MCP](https://modelcontextprotocol.io/specification/2026-07-28) quan reviseu un servidor nou.

L'URL de l'especificació del 2025-06-18 al paràgraf de context següent és una versió històrica. Utilitzeu l'especificació del 2026-07-28 per a les noves revisions.

[El estàndard MCP](https://modelcontextprotocol.io/specification/2025-06-18) estandarditza les connexions entre una aplicació LLM, un connector de client i un servidor. Un servidor ofereix eines, recursos o indicacions (prompts). L'especificació també estableix que els amfitrions han d'obtenir el consentiment de l'usuari abans d'exposar dades o d'invocar eines.

**El mateix MCP no atorga permisos.** Una eina MCP continua executant-se dins dels permisos del procés del servidor, de l'usuari del sistema operatiu, de la ruta de xarxa, del compte de núvol i de les credencials configurades. Una descripció d'eina no és una política d'autorització.

La [documentació de 1Password Security for AI](https://www.1password.dev/security-for-ai) descriu un servidor MCP d'Entorns i patrons de configuració segura de MCP. La mateixa pàgina descriu la càrrega en temps d'execució dels valors de configuració de MCP des de 1Password. Aquestes pàgines no defineixen un producte MCP genèric de claus SSH de 1Password ni un flux de treball SSH universal per a cada client d'agent.

Utilitzeu MCP com a superfície de control estreta:

- **Eines de lectura:** Inspeccioneu l'estat del servei, les metadades del repositori o els registres aprovats.
- **Eines de planificació:** Prepareu un comandament o un registre de canvis sense executar el comandament.
- **Eines d'aprovació:** Sol·liciteu una decisió humana abans d'una escripta remota.
- **Eines d'escripta:** Mantingueu-les desactivades fins que el destí, el comandament, l'abast i el pla de reversió siguin explícits.

L'agent hauria de rebre referències, metadades i resultats d'operacions. **L'agent no hauria de rebre el text de la clau privada, un volcat de tots els elements d'un cofre ni un shell il·limitat.**

## Una primera política segura

Comenceu amb una política escrita abans d'activar un agent. Mantingueu la política propera a la configuració de MCP, però no placeu credencials al fitxer.

```yaml
agent_policy:
  purpose: "Read-only repository and system inspection"
  identities:
    interactive_ssh: "1Password SSH Agent with per-terminal consent"
    unattended_jobs: "Dedicated service account with one narrow vault"
  allowed:
    - "Read repository metadata through Git"
    - "Read approved service status and logs"
    - "Run one synthetic SSH connectivity check"
  approval_required:
    - "Any remote write"
    - "Any package, firewall, clock, or service change"
    - "Any new host-key acceptance"
    - "Any private-key export"
  denied:
    - "Read or print private-key fields"
    - "List every vault or every item"
    - "Write tokens or secrets to shell profiles"
    - "Run arbitrary commands from tool output"
  rollback:
    - "Revoke the service account"
    - "Remove the public key from the target"
    - "Disable the MCP server entry"
    - "Lock 1Password and end the agent session"
```

Aquesta política és un exemple, no un format de configuració de 1Password. Emmagatzemeu la política real al pla de control utilitzat pel vostre client d'agent. Reviseu cada eina contra la política abans d'activar cada eina.

## Comptes de servei i referències de secrets

Un **compte de servei** atorga a un procés automatitzat la seva pròpia identitat. La [guia de scripts de la CLI de 1Password](https://www.1password.dev/cli/secrets-scripts) recomana els comptes de servei per a l'accés amb el mínim de privilegis a cofres seleccionats. Això separa una tasca no atesa de la SSO, MFA, el inventari de cofres i el compte diari d'una persona.

Una **referència secreta** designa un valor sense incloure'l al codi font. La [referència de la CLI de 1Password](https://www.1password.dev/cli/reference) utilitza la forma `op://vault/item/field`. La referència és segura d'emmagatzemar només quan el procés circumdant continua tenint un accés restringit. Una referència no eludeix la política.

Utilitzeu `op read` quan un únic comandament necessita un únic valor. Utilitzeu `op run` quan un procés fill necessita un conjunt controlat de valors d'execució. Utilitzeu `op item create` quan cal que un nou element de clau SSH existeixi al cofre aprovat.

No confongueu la injecció d'execució amb la protecció de la clau privada. Un testimoni d'API transmes com a variable d'entorn continua sent visible pel procés fill. Una clau privada transmesa a través d'una variable d'entorn és pitjor, ja que el valor amplia l'exposició a la inspecció de processos, els informes de fallides, la sortida de depuració, el seguiment de la shell i els registres accidentals.

**Preferiu una referència al codi font i un valor d'execució al procés més petit possible.** Mantingueu el procés de vida curta. Desactiveu el seguiment de la shell. No imprimeu l'entorn. Elimineu els fitxers temporals després d'una execució fallida.

## Flux de treball segur inicial

La seqüència següent separa el registre de la clau pública, l'SSH interactiu, la descoberta MCP i el disseny no supervisat.

### 1. Definir la destinació

Anoteu la classe de destinació, el compte remot, el repositori o comandament previst, l'origen de la clau de l'amfitrió, el propietari de l'aprovació i l'acció de reversió. Utilitzeu un registre sintètic durant el primer exercici.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Resultat esperat, no provat:** El registre identifica una destinació i una operació. El registre no conté un nom d'amfitrió, una adreça IP, un testimoni, una clau privada ni dades personals.

### 2. Crear o seleccionar l'element de clau SSH

La [guia oficial de claus SSH de 1Password](https://www.1password.dev/ssh/manage-keys) documenta el patró de creació de la CLI. El comandament següent utilitza un títol sintètic i un cofre de proves anomenat.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Sortida esperada, no provada:** 1Password crea un element de clau SSH al cofre de proves anomenat i oculta la clau privada a la sortida de la terminal. El comandament modifica l'estat de 1Password. La sortida llegible per a humans exacta depèn de la versió de la CLI i de l'estat d'inici de sessió.

Captureu l'identificador de l'element retornat al registre de proves sense copiar el camp de la clau privada. Utilitzeu l'identificador o el títol exacte de l'element per a lectures específiques de camps només després de confirmar l'esquema de l'element.

No redirigiu aquesta sortida a un registre compartit. Captureu només l'identificador de l'element, la empremta de la clau pública i el registre d'aprovació quan el procediment local admet una sortida estructurada segura.

### 3. Gestionar la clau pública

Obriu l'element Clau SSH a 1Password i utilitzeu l'acció Copiar clau pública. Utilitzeu una referència específica de camp només després de confirmar l'etiqueta del camp de clau pública al vostre propi compte. No aboqueu l'element complet.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Sortida esperada, no provada:** Una línia sintètica de clau pública OpenSSH o un valor de clau pública del camp confirmat. El nom del camp de marcador de posició anterior no és una promesa sobre l'etiqueta del camp del vostre element.

Registreu la clau pública al compte de Bitbucket aprovat, al repositori de Bitbucket o al compte remot. Mai enganxeu la clau privada corresponent a Bitbucket. La [guia SSH de Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) també recomana registrar la clau d'amfitrió de Bitbucket abans de la primera connexió.

Per a Bitbucket, obteneu el registre de clau d'amfitrió publicat i compareu el registre amb una còpia de confiança independent abans d'afegir una línia a `~/.ssh/known_hosts`. Utilitzeu la comprovació estricta de l'amfitrió després que la comparació sigui correcta. No accepteu una clau d'amfitrió modificada durant l'execució d'un agent.

### 4. Habilitar SSH interactiu

Activeu l'Agent SSH de 1Password a l'aplicació d'escriptori. Configureu OpenSSH amb el valor `IdentityAgent` o `SSH_AUTH_SOCK` específic de la plataforma de la [guia oficial de configuració](https://www.1password.dev/ssh/get-started). Limiteu la primera prova a un sol repositori o a un sol compte no de producció.

A macOS o Linux, establiu el socket des de la guia de configuració de la plataforma i executeu `ssh-add -l`. A Windows, utilitzeu la configuració de tub anomenat admissible i verifiqueu les claus disponibles a través de la interfície de l'Agent SSH de 1Password o una prova SSH de Windows documentada. No presenteu `ssh-add -l` com a comanda de verificació multiplataforma.

Només a macOS o Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Sortida esperada, no provada:** A macOS o Linux, `ssh-add -l` llista les empremtes digitals de l'agent actiu. A Windows, utilitzeu la prova de tub anomenat documentada o la interfície de l'Agent SSH de 1Password. Una lectura d'èxit de Git retorna una referència de commit. El marcador de posició del repositori anterior requereix substitució en una prova controlada.

La comanda utilitza un marcador de posició de repositori. Substituiu el marcador de posició només en una prova controlada. **No aproveu una sol·licitud per a un objectiu o procés que no esperàveu.**

### 5. Afegir MCP després que la ruta SSH funcioni

Primer verifiqueu el client SSH i l'objectiu sense MCP. Després afegiu un sol servidor MCP de només lectura o un connector local. Doneu a l'agent una eina com `read_status` o `prepare_command`. No comenceu amb una eina de shell general.

La configuració de l'MCP hauria de fer referència als valors d'execució mitjançant el mecanisme d'entorn admes pel client. La [Guia de seguretat de 1Password AI](https://www.1password.dev/security-for-ai)] descriu la substitució dels tokens de configuració MCP en text pla per variables d'entorn carregades des de 1Password. **Mantingue la referència o el nom de la variable a la configuració. Mantingui el valor resolt fora de la transcripció de l'agent.**

Aquesta secció descriu un disseny, no una configuració MCP provada. Aquí no es fixa cap client, servidor, transport, versió o fixture. Valideu un servidor només de lectura en un perfil de proves separat abans de connectar un agent a un sistema de producció.

### 6. Registre del resultat

Registreu la classe objectiu, el nom de l'eina, la decisió d'aprovació, la petjada de la clau pública, el resultat de la comanda i el resultat de la neteja. Ometeu els valors secrets. Marqueu cada sortida com a observada o esperada.

**Resultat esperat, no provat:** L'agent llegeix l'estat, proposa una comanda acotada, rep l'aprovació explícita per a la sol·licitud SSH, completa l'operació només de lectura i genera un registre sense text de la clau privada.

## Seqüència de comandes sintètica

La següent seqüència mostra l'ordre sense utilitzar infraestructura real. Aquestes comandes són només exemples. No s'han executat durant la preparació de l'article.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Sortida esperada, no provada:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

El bloc de sortida és il·lustratiu. El bloc no representa una execució contra un compte de 1Password, Bitbucket, un proveïdor de Git o un amfitrió remot. Un registre de producció hauria d'emmagatzemar només metadades aprovades i un estat d'èxit o fallida.

## Accés interactiu versus no atès

| Mode d'accés | Identitat | Camí de la clau privada | Model d'aprovació |
|---|---|---|---|
| **SSH interactiu** | Compte humà a través de l'Agent SSH de 1Password | La clau privada es manté a l'aplicació de 1Password | Un humà aprova un procés, una sessió de terminal o una sol·licitud |
| **Lectura programada** | Compte de servei dedicat | `op run` subministra valors d'execució acotats | Política de tasques i abast del compte de servei |
| **SSH programat** | Identitat d'automatització dedicada | L'exportació de la clau continua sent un disseny d'últim recurs | Aïllament de tasques, vida útil curta, restricció d'amfitrió i rotació |
| **Escriptura d'agent** | Identitat humana o específica de la tasca | Depèn de la integració aprovada | Aprovació humana abans de cada canvi definit |

*No programis un flux de treball al voltant d'un prompt de l'Agent SSH interactiu. Utilitzeu un disseny d'automatització separat o mantingueu el pas operat per un humà.*

Per a les tasques no ateses, creeu un compte de servei amb accés a un sol cofre o a un petit conjunt d'elements. Doneu a la tasca un únic propòsit. Utilitzeu un repositori o un compte de servidor dedicat. Afegiu la verificació de la clau d'amfitrió. Establiu un temps d'execució màxim. Registreu les metadades de les accions sense secrets. Revoqueu o rotateu la identitat després de la prova.

Si una tasca no atesa necessita realment una clau privada SSH, utilitzeu una clau d'automatització dedicada amb un compte remot estret i una data de finalització documentada. Obtenir la clau privada amb `op read` encara exporta el material de la clau a través d'un límit de procés. Aquest disseny té un radi d'impacte més gran que l'Agent SSH de 1Password. Preferiu una identitat de plataforma, un servei de desplegament o una altra identitat de càrrega de treball quan el destí ho suporti.

## Per què les variables d'entorn en text pla augmenten el risc

Les variables d'entorn mantenen els secrets fora dels fitxers de codi font, però no fan que els secrets siguin invisibles. Un procés fill llegeix el seu entorn. La inspecció de processos, els gestors de fallides, la sortida de depuració, el seguiment de la shell i els registres copiats d'ordres podrien exposar els valors.

1Password documenta `op run` com a mètode d'execució per carregar referències en un subprocés. Utilitzeu `op run` per als valors que un procés necessita realment. Manteniu el procés fill de vida curta i restringiu la seva ordre. No passeu una clau privada a través de `SSH_PRIVATE_KEY`, `KEY` o una variable similar quan l'Agent SSH elimina la necessitat d'exportar-la.

L'ordre més segura és:

1. **Utilitzeu l'Agent SSH** per a SSH interactiu.
2. **Utilitzeu el registre de clau pública** per a Bitbucket o el compte remot.
3. **Utilitzeu `op run`** per a un procés fill no atès estret.
4. **Utilitzeu `op read`** per a un sol valor quan un procés fill no necessita un entorn complet.
5. **Exporteu una clau privada** només després d'una excepció per escrit, un àmbit estret, un pla de neteja i un pla de rotació.

## Taula de decisions

| Necessitat | Camí preferit | Motiu per aturar o redissenyar |
|---|---|---|
| Una persona executa Git sobre SSH | 1Password SSH Agent | Aturar si el prompt nomena un procés o una clau inesperats |
| Registrar una clau de repositori | Llegir o omplir automàticament la clau pública | Mai copiar la clau privada al servei de repositoris |
| L'agent llegeix l'estat del servei | Eina MCP només de lectura amb abast al nivell del SO | Aturar si l'eina exposa una shell il·limitada |
| L'agent proposa un canvi remot | Eina de planificació seguida d'aprovació humana | Aturar si l'objectiu, la comanda o el retrocés no són clars |
| Una tasca llegeix un token d'API | Compte de servei més `op read` o `op run` | Aturar si el token entra al codi font, als registres o a un perfil global |
| Una tasca necessita accés SSH | Identitat de càrrega de treball o clau d'automatització dedicada | Aturar si la tasca requereix una clau personal o un compte ampli |
| La configuració MCP necessita un token | Referència d'execució carregada pel client admissible | Aturar si un token en text pla es commita a la configuració |

## Gestió de fallades

**Prompt de consentiment SSH inesperat:** Negar el prompt. Comprovar el nom del procés, la sessió de terminal, la petjada de la clau, l'objectiu del repositori i la clau de l'amfitrió. Revisar la configuració del client SSH abans de tornar-ho a provar.

**No hi ha el socket de l'agent SSH:** Confirmar que l'aplicació d'escriptori de 1Password està instal·lada mitjançant un mètode admissible, que l'agent SSH està habilitat i que el client utilitza el socket específic de la plataforma. La [pàgina oficial de l'agent SSH](https://www.1password.dev/ssh/agent) llista els requisits del sistema operatiu i els enllaços de configuració del socket.

**L'autenticació per clau pública falla:** Comprovar la clau pública seleccionada, el compte remot, el permís del repositori, la clau de l'amfitrió i la configuració SSH. Utilitzar una comparació de petjades públiques. No resoldre l'error exportant una clau privada no relacionada.

**`op read` denega l'accés:** Comprovar l'abast de la bóveda del compte de servei, l'identificador de l'element, la referència del camp, l'estat d'inici de sessió i l'estat de l'element. Reduir la referència a un únic element aprovat. No ampliar la concessió de la bóveda com a primera resposta.

**`op run` exposa un valor:** Aturar la tasca. Conservar només el registre mínim de l'incident. Eliminar els registres copiats i els fitxers temporals segons el vostre procediment de retenció. Rotar el secret o la clau afectats. Revisar la traça de la shell, la inspecció de processos, els informes de fallada i la retenció del transcricpt MCP.

**El comportament de l'eina MCP és inesperat:** Tracta la sortida de l'eina com a dades no fiables. Atura't abans d'executar les ordres suggerides per la sortida. Inspecciona el codi font del servidor, la configuració, els permisos i el transport. L'amfitrió MCP ha d'obtenir el consentiment de l'usuari. L'especificació també proporciona orientacions per als implementadors sobre el consentiment i els controls d'accés, però el protocol no substitueix la teva revisió.

## Reversió i eliminació

La reversió comença amb l'eliminació de l'accés, no amb la supressió de fitxers.

1. **Atura l'agent o la tasca programada.** Desactiva l'entrada del servidor MCP o desconeix el client.
2. **Bloqueja 1Password.** Finalitza la sessió d'autorització SSH interactiva.
3. **Elimina la clau pública.** Suprimeix la clau de prova de Bitbucket, el repositori o el compte remot.
4. **Revoca el compte de servei.** Elimina el seu accés al cofre i invalida el seu testimoni.
5. **Suprimeix l'element de la clau SSH de prova** després de confirmar que cap flux de treball aprovat utilitza aquest element.
6. **Elimina la configuració temporal.** Suprimeix les referències de prova, les substitucions de socket local i els registres generats.
7. **Revisa les proves.** Assegura't que el registre de reversió no conté cap clau privada, testimoni o volcat de l'entorn.

*Suprimir un fitxer local no revoca una clau pública, un compte de servei, un testimoni en memòria cau o una autorització remota. Elimina cada concessió a la seva font.*

## Solució de problemes

### L'agent demana una clau en cada ordre

Comprova l'abast d'autorització seleccionat. L'aprovació per sol·licitud és més restrictiva. Potser la sessió del terminal o de l'aplicació s'ha acabat. 1Password també demana de nou després d'un esdeveniment de bloqueig o sortida.

### L'agent veu una clau privada al seu transcendent

Atura el flux de treball i rota la clau. Inspecciona la resposta del servidor MCP, l'ordre del shell, el registre de depuració i el contenedor de l'eina. Substitueix les lectures de claus privades per l'ús de SSH Agent per a tasques interactives. Per a les tasques, substitueix una clau personal per una identitat dedicada i una excepció documentada.

### Una llista de claus conté massa identitats

L'agent SSH de 1Password exposa les claus admeses dels seus cofres configurats. Utilitza una configuració d'agent amb abast definit o una configuració SSH específica de l'amfitrió. La [documentació de l'agent](https://www.1password.dev/ssh/agent) també assenyala el límit de sis claus del servidor OpenSSH.

### Una ordre funciona manualment però falla en una tasca

Compara la identitat, l'abast del cofre, l'entorn, les dades de la clau de l'amfitrió, el directori de treball i les suposicions d'aprovació. Una sessió interactiva de 1Password inclou el consentiment humà. Una tasca programada no. Disseny la tasca com un mode d'accés separat.

### El servidor MCP està connectat però la tasca falla

La connexió no demostra l'autorització. Comproveu la detecció d'eines, les credencials del servidor, el consentiment del client, els permisos del sistema operatiu, l'accés a la xarxa i els permisos del costat de destinació en passos separats. Manteniu la primera prova només de lectura.

## Passos següents

Utilitzeu l'especificació MCP actual del 2026-07-28 per a les noves aprovacions. Qualsevol enllaç a l'especificació del 2025-06-18 d'aquest article és context històric.

Comenceu amb un repositori sintètic i una eina MCP només de lectura. Registreu cada resultat esperat com a no provat fins que un entorn controlat generi evidències. A continuació, repeteix el flux de treball amb un objectiu no de producció, un operador nomenat, una clau de servidor verificada i un registre escrit de retrocés.

Llegiu la [referència de la CLI de 1Password](https://www.1password.dev/cli/reference) per als paràmetres de comandament actuals. Llegiu [Carregar secrets en scripts](https://www.1password.dev/cli/secrets-scripts) abans de crear automatitzacions de comptes de servei. Llegiu l'[especificació MCP](https://modelcontextprotocol.io/specification/2026-07-28) abans d'aprovar eines d'un servidor nou.

**Manteniu SSH interactiu aprovat per humans. Manteniu l'accés no atès separat. Manteniu les claus privades no llegibles sempre que l'objectiu admeti autenticació basada en agent.**
