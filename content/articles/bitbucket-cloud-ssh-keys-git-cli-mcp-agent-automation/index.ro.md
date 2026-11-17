---
title: "Chei SSH Bitbucket Cloud: acces Git doar în citire pentru agenți AI"
date: 2026-10-11
lastmod: 2026-11-09
toc: true
draft: false
description: "Configurați chei SSH Bitbucket Cloud, acces Git CLI, tokenuri REST API, 1Password și instrumente MCP pentru fluxuri de lucru ale agenților AI doar în citire."
genre: ["Securitate cloud", "Instrumente pentru dezvoltatori", "Administrarea sistemelor"]
tags: ["Bitbucket Cloud", "chei SSH Bitbucket", "chei de acces la depozit", "chei de acces la proiect", "chei de acces la spațiul de lucru", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "scopuri token API", "permisiuni agenți", "automatizare doar în citire", "chei gazdă SSH"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "Flux de lucru în terminal care conectează accesul Git Bitbucket Cloud, chei SSH cu scop limitat, 1Password, citiri REST API și instrumente MCP"
coverCaption: ""
---

**Un flux de lucru limitat al agentului separă citirea depozitului, citirile API, gestionarea secretelor și scrierile la distanță.** Folosiți Git prin Secure Shell (SSH) pentru acces la surse, o cheie Bitbucket doar în citire pentru checkout automat, REST API pentru metadate și un server Model Context Protocol (MCP) pentru instrumente aprobate. Păstrați cheile private și tokenurile API în 1Password. Cereți aprobarea unei persoane înainte de scriere.

<!--more-->

## Idei principale

- **Doar în citire în mod implicit:** folosiți o cheie de acces la depozit sau proiect pentru checkout-ul agentului. Niciuna nu permite push.
- **Identitate personală:** folosiți o cheie SSH personală pentru lucrări interactive asociate unui cont de utilizator.
- **Custodia secretelor:** folosiți 1Password SSH Agent pentru ca Git să solicite o operație de semnare autorizată fără să citească cheia privată.
- **Sensul CLI:** considerați `git`, `curl` și un wrapper API mic, auditat, drept linia de comandă practică pentru Bitbucket.
- **Limita MCP:** expuneți instrumente de citire cu domeniu restrâns. Dezactivați instrumentele de scriere sau plasați-le în spatele unei aprobări separate.
- **Controlul scrierii:** permiteți agentului să inspecteze, să compare și să pregătească o modificare. Cereți aprobarea unei persoane înainte de push, pull request, merge sau actualizarea setărilor.

## Înainte de a începe

**Cerințe:** acces la Bitbucket Cloud, Git, un client OpenSSH, 1Password 8, 1Password CLI, o CLI conectată sau un cont de serviciu aprobat și o gazdă MCP cu controale de aprobare a serverelor. Rezervați 45 de minute. Dificultate medie.

Folosiți un depozit de test pentru prima încercare. Înlocuiți fiecare substituent din exemple. Comenzile de mai jos sunt exemple netestate. Nu reprezintă un cont sau un depozit Bitbucket activ.

**Versiuni:** articolul oferă recomandări de proiectare, nu o procedură legată de anumite versiuni. Înainte de testare, confirmați versiunile instalate de Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, gazda MCP și serverul MCP. Configurați 1Password SSH Agent pentru sistemul de operare actual înainte să folosiți `ssh-add -l`.

**Nu păstrați acreditările în shell-uri, jurnale, URL-uri, remote-uri Git sau fișiere sursă.** Folosiți substituenți precum `<workspace>`, `<repository>`, `<api-token>` și `<socket-path>`. Nu lipiți o cheie privată reală într-o transcriere de terminal.

## Alegeți limita de acces

Bitbucket Cloud acceptă chei de acces la nivel de depozit, proiect și spațiu de lucru. Domeniul cheii schimbă impactul copierii ei. [Comparația oficială a cheilor de acces](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) explică direct diferențele de permisiuni.

| Cale de acces | Domeniu | Permite scrierea | Utilizare potrivită |
|---|---|---:|---|
| **Cheie de acces la depozit** | Un depozit | Nu | Checkout implicit pentru agent |
| **Cheie de acces la proiect** | Depozitele dintr-un proiect | Nu | Lucrări doar în citire pentru un grup mic de depozite |
| **Cheie de acces la spațiul de lucru** | Depozitele dintr-un spațiu de lucru | Da | Automatizare de serviciu controlată, cu plan separat de scriere |
| **Cheie SSH personală** | Depozitele permise unui utilizator | Urmează contul utilizatorului | Administrare interactivă |
| **Token API** | Scopuri API și acces la cont asociate utilizatorului | Depinde de scopuri | Citiri REST API sau o sarcină temporară de scriere |

**Începeți cu cea mai mică limită utilă.** Alegeți o cheie de depozit dacă este suficient un singur depozit. Alegeți o cheie de proiect dacă mai multe depozite aparțin aceluiași proiect și accesul doar în citire este suficient. Tratați o cheie de spațiu de lucru ca identitate de scriere, nu ca opțiune implicită comodă.

Creați și înregistrați cheia cu cele mai mici permisiuni prin calea potrivită din setările Bitbucket:

1. Pentru un depozit, deschideți Repository settings, Access keys și Add key. Lipiți cheia publică și păstrați cheia doar în citire.
2. Deschideți Project settings, Access keys și Add key când mai multe depozite au nevoie de o identitate de citire cu domeniu de proiect.
3. Folosiți o cheie de spațiu de lucru doar într-un spațiu partajat cu un plan de scriere aprobat. Spațiile de lucru personale nu oferă aceeași cale la nivel de spațiu.
4. Notați eticheta cheii, domeniul, amprenta cheii publice, proprietarul și data rotirii. Păstrați cheia privată în 1Password.

După înregistrare, rulați un test exact de conexiune doar în citire:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**Rezultat așteptat:** o referință de commit pentru `HEAD`. Exemplu netestat. Un rezultat reușit dovedește că o identitate SSH permisă a ajuns la depozitul indicat. Nu dovedește că a fost selectată cheia înregistrată sau că există acces de scriere. Repetați testul după configurarea unei chei pentru fiecare depozit.

Pentru custodia cheilor private și consimțământul 1Password SSH Agent, consultați [1Password CLI și SSH Agent: chei SSH securizate pentru agenți AI](/articles/1password-cli-ssh-keys-mcp-agent-administration/).

## Definiți corect „Bitbucket CLI”

Expresia **Bitbucket CLI** amestecă adesea trei interfețe diferite. Păstrați-le separate.

- **Git CLI:** `git clone` și `git fetch` transferă datele depozitului prin SSH sau HTTPS. `git diff` compară fișiere locale sau revizii.
- **Client REST:** `curl` sau un wrapper revizuit apelează API-ul Representational State Transfer (REST) al Bitbucket Cloud. Un API este o interfață programatică pentru solicitarea datelor sau acțiunilor. [Referința Bitbucket Cloud REST API](https://developer.atlassian.com/cloud/bitbucket/rest/) enumeră resurse pentru depozite, surse, ramuri, pull request-uri, pipeline-uri și stări.
- **Atlassian CLI:** `acli` este linia de comandă oficială Atlassian. [Introducerea](https://developer.atlassian.com/cloud/acli/guides/introduction/) descrie produsul, iar [referința de comenzi](https://developer.atlassian.com/cloud/acli/reference/commands/) enumeră suprafețele `admin`, `jira`, `feedback` și `rovodev`. Referința nu documentează comenzi Bitbucket Cloud.

**Referința oficială de comenzi `acli` Atlassian nu documentează comenzi Bitbucket Cloud.** Nu inventați o comandă precum `acli bitbucket clone`. Folosiți Git pentru operațiile Git și REST API pentru datele Bitbucket Cloud.

### Teamwork Graph CLI opțională

**Atlassian publică și Teamwork Graph CLI, numită `twg`.** [Prezentarea](https://developer.atlassian.com/cloud/twg-cli/) și [catalogul de comenzi](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) documentează familii de comenzi Bitbucket. Comanda de configurare este:

```bash
twg setup
```

Comanda de configurare schimbă starea locală de autentificare. Urmați solicitările versiunii instalate pentru configurarea opțională a tokenului Bitbucket. Calea tokenului Bitbucket din CLI este separată de Atlassian OAuth. Păstrați sintaxa exactă a comenzii sincronizată cu versiunea instalată și catalogul actual. Folosiți un profil separat, un token restricționat, competențe instalate revizuite și aprobare umană pentru comenzile care modifică date.

**Rezultat așteptat, netestat:** profilul izolat primește setările de autentificare Bitbucket. Înregistrați starea anterioară a profilului înainte de configurare. Pentru revenire, eliminați acreditarea salvată prin procedura documentată de deconectare sau eliminare a configurației pentru versiunea instalată.

Dacă un proiect terț se numește Bitbucket CLI, auditați sursa, procesul de lansare, sumele de control, calea de actualizare, fluxul de autentificare, scopurile cerute, destinațiile de rețea, gestionarea jurnalelor și comenzile de scriere. Un nume familiar de binar nu demonstrează suportul furnizorului sau permisiuni sigure.

## Păstrați cheile SSH sub controlul 1Password

[1Password SSH Agent](https://www.1password.dev/ssh/agent) pune la dispoziția Git și a clienților SSH cheile SSH stocate în 1Password. Clientul efectuează o cerere de semnare autorizată. Cheia privată rămâne în aplicația 1Password, iar 1Password cere consimțământ înainte ca un client aprobat să folosească o cheie.

[Referința 1Password CLI](https://www.1password.dev/cli/reference) are alt rol. Folosiți `op` pentru acces controlat la elemente, tokenuri API, conturi de serviciu și configurarea automatizării. Folosiți SSH Agent pentru semnarea SSH. Evitați exportarea unei chei private într-un fișier temporar doar pentru a simplifica fluxul agentului.

Verificați starea locală a CLI și a agentului cu comenzi doar în citire:

```bash
op --version
ssh-add -l
```

**Rezultat așteptat:** o versiune 1Password CLI și una sau mai multe amprente de chei publice ale agentului activ. Exemplu netestat. Un rezultat gol pentru `ssh-add -l` înseamnă că nu este disponibilă nicio cheie prin socketul agentului selectat.

Pentru o cheie nouă, creați un element SSH Key Ed25519 în 1Password sau importați o cheie generată printr-un proces local de încredere. Alegeți o etichetă după scop, domeniu și data rotirii. Adăugați doar cheia publică în Bitbucket Cloud. [Ghidul Linux pentru cheile de acces la depozite](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) descrie calea din setările depozitului și limita doar în citire.

## Verificați mai întâi cheia gazdă Bitbucket

Autentificarea utilizatorului SSH nu dovedește identitatea serverului. Clientul trebuie să verifice cheia gazdă Bitbucket Cloud înainte să trimită o cerere de autentificare. [Ghidul Atlassian pentru SSH și verificarea în doi pași](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) enumeră cheile gazdă publice și arată endpointul oficial pentru obținerea intrărilor known-hosts.

Preluați datele publice ale cheii gazdă pentru comparație:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**Rezultat așteptat:** linii OpenSSH `known_hosts` pentru `bitbucket.org`. Exemplu netestat. Comparați cheia sau amprenta returnată cu o copie independentă de încredere înainte de a adăuga linia în `~/.ssh/known_hosts`.

Folosiți verificarea strictă a gazdei după ce există intrarea aprobată:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**Nu acceptați o cheie gazdă schimbată în timpul rulării agentului.** Opriți rularea, verificați registrul actual al cheilor gazdă Bitbucket Cloud și examinați intrarea locală `known_hosts`. Acceptarea automată elimină o limită de securitate bazată pe chei.

## Selectați o cheie pentru fiecare depozit

Un dispozitiv are adesea mai multe chei Bitbucket. Un agent SSH general oferă mai multe identități la o conexiune. Un server sau o politică cu o limită mică de încercări de autentificare ar putea respinge cheia corectă după eșecul celor anterioare.

[Ghidul Atlassian pentru mai multe chei de acces la depozite](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) folosește `core.sshCommand` într-un fișier de configurare Git al depozitului și `includeIf` în configurația Git globală. Urmați același model pentru o cheie per depozit.

Exemplu portabil bazat pe fișiere:

```ini
# .gitconfig inside one local repository
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

Blocul de mai sus este o excepție cu fișier de cheie privată pentru o identitate de automatizare dedicată. Nu configurează 1Password SSH Agent. Pentru 1Password SSH Agent, configurați valoarea `IdentityAgent` sau `SSH_AUTH_SOCK` specifică platformei din [ghidul de configurare 1Password](https://www.1password.dev/ssh/get-started). Unele configurații OpenSSH folosesc un fișier `.pub` ca selector de identitate a agentului. Confirmați suportul platformei înainte să îl folosiți. O configurare bazată pe fișier cere calea cheii private corespunzătoare. Nu transmiteți niciodată un fișier `.pub` unei comenzi care cere material de cheie privată și nu exportați o cheie privată personală.

Folosiți o configurare explicită a depozitului când o clonă locală are nevoie de o anumită cheie. Folosiți `includeIf` când un director conține mai multe clone cu aceeași limită de acces. [Ghidul pentru mai multe chei](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) arată ambele setări în fluxul Bitbucket.

Clonați cu Git prin SSH:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**Rezultat așteptat:** Git creează `<local-directory>` și preia depozitul prin `bitbucket.org`. Exemplu netestat. O cheie de acces la depozit permite doar clonarea și pull.

## Folosiți tokenuri API pentru citiri REST restrânse

Folosiți SSH pentru transportul Git. Folosiți REST API pentru metadate sau operații din afara transportului Git. [Ghidul permisiunilor tokenurilor API](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) enumeră scopuri de depozit precum Read, Write, Admin și Delete. Repository Read corespunde `read:repository:bitbucket` și nu include acces la pull request-uri.

Pentru automatizare în citire, preferați un token de acces la depozit sau proiect Bitbucket dacă ținta acceptă endpointul necesar. Un token API asociat unui utilizator păstrează accesul mai larg al contului. Folosiți un token de spațiu de lucru doar când înregistrarea sarcinii specifică această limită mai largă. Consultați [ghidul tokenurilor de acces Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) înainte să alegeți tipul.

Pentru citirea de către agent, începeți cu `read:repository:bitbucket`. Adăugați `read:pullrequest:bitbucket` doar când agentul are nevoie de date despre pull request-uri. Adăugați scopuri de spațiu de lucru sau pipeline numai dacă înregistrarea sarcinii indică endpointul și rezultatul. Scopurile Write și Admin necesită o cale separată de aprobare.

Creați fiecare token API pentru un singur scop, setați data expirării, notați-o în registrul de rotire și înlocuiți tokenul înainte de expirare. [Ghidul Atlassian pentru crearea unui token API](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) cere nume, dată de expirare, selectarea aplicației și scopuri. Tokenul este afișat o singură dată după creare.

Păstrați valoarea în 1Password sau într-un secret de runtime gestionat. Nu o includeți într-un URL la distanță. Trimiteți tokenul bearer printr-o variabilă de mediu doar procesului care are nevoie de o singură citire:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

Păstrați `/path/to/agent.env` în afara depozitului. În fișier, stocați o referință precum `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential`. `op run` rezolvă referința și expune valoarea procesului copil curl pe durata subprocesului. Nu împiedică procesul copil să citească valoarea variabilei de mediu sau să o scrie într-un jurnal. Nu înlocuiți substituentul cu un token literal.

**Rezultat așteptat:** metadate JSON pentru depozitul selectat. Exemplu netestat. Substituentul nu trebuie să devină niciodată un token real într-un fișier comis sau jurnal.

Pentru automatizări mai lungi, permiteți ca 1Password să injecteze un secret în mediul procesului prin fluxul CLI sau de cont de serviciu acceptat. Păstrați durata tokenului potrivită sarcinii. Revocați tokenul dacă sarcina se încheie mai devreme sau se schimbă proprietarul gazdei.

## Oferiți MCP o suprafață mică de citire

Folosiți [specificația MCP actuală](https://modelcontextprotocol.io/specification/2026-07-28) și [regulile de autorizare](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) când examinați un server nou. Serverele HTTP trebuie să verifice audiența tokenului și să gestioneze clar răspunsurile 401 și 403.

Gazda MCP obține consimțământul utilizatorului. Clientul menține o conexiune la un server. Serverul expune instrumente, resurse sau prompturi. Tratați fiecare server drept cod neîncredere până când îi verificați sursa, transportul, contul și permisiunile.

URL-ul specificației 2025-06-18 din paragraful următor este o versiune istorică. Folosiți versiunea actuală 2026-07-28 pentru recenziile noi.

[Specificația MCP](https://modelcontextprotocol.io/specification/2025-06-18) definește comunicarea dintre o gazdă MCP, un client și un server. Un server expune instrumente, resurse sau prompturi prin protocol. MCP standardizează formatul conexiunii. Gazda, implementarea serverului, contul, domeniul tokenului și politica de aprobare decid totuși ce poate accesa un apel.

Folosiți un server MCP ca adaptor restrâns peste Git și Bitbucket Cloud REST API.

Protejați adaptorul împotriva transmiterii tokenurilor, falsificării cererilor pe partea serverului (SSRF) și comportamentului de delegat confuz. SSRF permite unui server să trimită cereri către destinații neintenționate. Un delegat confuz apare când serverul folosește privilegii mai largi în numele apelantului. Protejați-l și de servere locale rău intenționate, redirecționări OAuth nesigure și răspunsuri prea mari cu date sursă. Fixați originile Bitbucket permise și identificatorii depozitelor. Rulați serverele locale într-un sandbox, sub un utilizator de sistem dedicat. Redactați secretele din rezultatele instrumentelor și jurnale.

Această secțiune descrie un proiect, nu o configurație MCP testată. Nu este fixat niciun client, server, transport, versiune sau fixture. Validați un server doar în citire într-un profil de test separat înainte să conectați un agent la un depozit de producție.

Exemple de instrumente de citire:

| Instrument | Rezultat limitat |
|---|---|
| **`get_repository_metadata`** | Returnează metadatele unui depozit |
| **`read_source_file`** | Citește o cale la o revizie |
| **`list_branches`** | Listează ramurile unui depozit |
| **`get_pull_request`** | Returnează un pull request dacă tokenul are scop de citire pentru pull request-uri |
| **`get_build_status`** | Returnează datele de stare ale unui commit |

Aceste denumiri descriu un proiect. Nu sunt comenzi Atlassian. Nu permiteți serverului să accepte URL-uri arbitrare, comenzi shell arbitrare, tokenuri brute, cereri de exportare a cheilor private sau identificatori de depozit fără restricții.

Setați permisiunile pe patru niveluri:

1. **Bitbucket Cloud:** cheie de citire la nivel de depozit sau proiect pentru Git, plus cele mai mici scopuri API necesare pentru citirile REST.
2. **1Password:** un seif sau cont de serviciu pentru sarcină, fără cale de exportare a cheilor private.
3. **Server MCP:** listă permisă de instrumente de citire, endpointuri Bitbucket Cloud fixe, validarea intrărilor, limite de timp și jurnale redactate.
4. **Gazdă MCP:** aprobarea utilizatorului pentru server și fiecare acțiune care poate scrie, cu instrumentele de scriere dezactivate în profilul implicit.

*O listă de instrumente MCP dovedește descoperirea lor. Nu dovedește autorizarea, scopul corect, tratarea sigură a intrărilor sau corectitudinea rezultatului.*

## Structurați fluxul agentului

Păstrați fluxul explicit. Fiecare etapă oferă dovezi pentru următoarea.

| Etapă | Acțiunea agentului | Permisiune | Control uman |
|---|---|---|---|
| **Pregătire** | Citește configurația, înregistrarea cheii gazdă, eticheta cheii, scopul tokenului și expirarea | Citire locală | Aprobă înregistrarea de configurare |
| **Inspectare** | Clonează sau face fetch prin Git peste SSH și interoghează metadate REST | Citire depozit și API | Nimic după configurare |
| **Analiză** | Citește fișiere, ramuri, pull request-uri și starea buildului prin instrumente aprobate | Instrumente MCP doar în citire | Nimic pentru citiri limitate |
| **Pregătirea modificării** | Produce un patch, un plan de ramură sau o schiță de pull request într-un spațiu local | Doar scriere locală | Verifică diff-ul și ținta |
| **Aprobarea scrierii** | Prezintă acțiunea exactă la distanță, domeniul și calea de revenire | Încă fără scriere la distanță | Aprobare umană |
| **Executarea scrierii** | Face push la o ramură, creează un pull request sau apelează un endpoint de scriere | Identitate de scriere cu durată scurtă | Confirmă fiecare acțiune |
| **Verificare** | Citește commitul, pull request-ul sau starea rezultată | Din nou doar în citire | Confirmă rezultatul așteptat |

Profilul implicit al agentului ar trebui să se oprească după **Analiză** sau **Pregătirea modificării**. Un profil separat de scriere ar trebui să folosească alt token sau altă cheie, expirare scurtă, țintă fixă și o solicitare de aprobare. O cheie de acces la depozit nu poate efectua pasul de scriere, ceea ce creează o limită tehnică utilă.

## Revenire și eliminare

Începeți revenirea prin eliminarea accesului, apoi curățați configurația locală:

1. Eliminați cheia de acces la depozit, proiect sau spațiu de lucru din pagina corespunzătoare de setări Bitbucket.
2. Revocați tokenul API de depozit, proiect, spațiu de lucru sau utilizator din pagina corespunzătoare de securitate Bitbucket.
3. Eliminați acreditarea Teamwork Graph salvată prin [procedura de autentificare documentată](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) pentru versiunea CLI instalată. Păstrați acreditarea anterioară doar în managerul de secrete aprobat. Confirmați că profilul izolat nu mai listează acreditarea de test.
4. După test, eliminați fișierul `.gitconfig` al depozitului și intrarea `includeIf`. Păstrați neschimbată configurația Git fără legătură.
5. Eliminați doar linia verificată a cheii gazdă Bitbucket adăugată pentru test. Păstrați celelalte chei gazdă aprobate.
6. Eliminați fișierul extern `agent.env` și ieșirea temporară. Eliminați intrarea serverului MCP din configurația gazdei, apoi reporniți gazda.

Înregistrați fiecare eliminare, operatorul și ora. Rotiți o cheie sau un token când o valoare apare într-un jurnal, registru de procese sau transcriere neașteptată.

## Buclă de citire la distanță cu actualizarea referințelor locale

Folosiți o buclă scurtă pentru inspectarea periodică a depozitului:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` este referința verificată în prezent în depozit. Un rezultat reușit dovedește că o identitate SSH permisă a ajuns la depozitul numit. Nu dovedește ce cheie a fost selectată sau dacă există acces push.

**Rezultat așteptat:** rezultatul fetch, starea ramurii și o linie de commit. Exemplu netestat. `fetch` nu scrie la distanță, dar actualizează referințele locale și `FETCH_HEAD`. Bucla nu face push și nu schimbă ramura.

Serverul MCP ar trebui să expună aceeași limită de citire prin operații numite. Un wrapper shell local sau un instrument MCP ar trebui să respingă un verb de scriere înainte de a trimite cererea. Înregistrați numele instrumentului, substituentul depozitului, revizia, clasa rezultatului și durata. Redactați tokenuri, cookie-uri, căi private și conținutul fișierelor, dacă sarcina nu cere explicit un anumit fișier.

## Depanare

### `Permission denied (publickey)`

Verificați socketul agentului activ, cheia publică selectată, intrarea cheii de acces la depozit și `IdentitiesOnly`. Cheia de depozit trebuie să existe în depozitul sau proiectul țintă. O cheie personală cere permisiuni de cont. O cheie de spațiu de lucru are altă limită de scriere.

### Este oferită cheia greșită pentru depozit

Folosiți o cheie per depozit prin `core.sshCommand` sau grupați clonele într-un director controlat de `includeIf`. Listați cheile agentului cu `ssh-add -l`. Dacă sunt disponibile multe chei 1Password, folosiți un selector de identitate explicit sau un marcaj SSH 1Password. [Ghidul 1Password Agent](https://www.1password.dev/ssh/agent) documentează numărul de chei și marcajele.

### SSH raportează o cheie gazdă schimbată

Opriți agentul. Nu ștergeți `known_hosts` ca prim răspuns. Comparați registrul actual al cheilor gazdă Bitbucket Cloud cu intrarea locală printr-un canal independent. Eliminați sau înlocuiți o intrare doar după ce comparația este validă.

### API returnează `401` sau `403`

Verificați expirarea și tipul tokenului, scopul endpointului și limita contului sau spațiului de lucru. Un scop de citire a depozitului nu include pull request-uri. Un endpoint de scriere cere scop de scriere și un profil de scriere aprobat. Nu extindeți scopurile până nu identificați endpointul care a eșuat.

### API returnează datele depozitului, dar nu și pull request-uri

Adăugați cel mai restrâns scop de citire a pull request-urilor la un token nou sau rotit. Nu reutilizați un token larg de utilizator pentru un server MCP doar în citire.

### Serverul MCP listează instrumente, dar un apel eșuează

Separați înregistrarea serverului, conexiunea, descoperirea instrumentelor, execuția și verificarea rezultatului. Inspectați jurnalul serverului fără a expune tokenul. Verificați endpointul și forma intrării. Încercați din nou o singură dată după verificarea conectivității. Marcați operația incompletă dacă al doilea apel eșuează.

### O CLI Bitbucket terță cere acces larg

Opriți instalarea. Comparați accesul cerut cu înregistrarea sarcinii. Examinați sursa, semnăturile sau sumele de control ale lansărilor, destinațiile de rețea, stocarea secretelor și comportamentul de scriere. Referința oficială a comenzilor Atlassian CLI nu demonstrează suport pentru un binar Bitbucket terț.

## Pașii următori

Creați un registru scurt de acces cu domeniul depozitului sau proiectului, eticheta cheii, data verificării cheii gazdă, scopurile API, expirarea tokenului, proprietarul 1Password, lista permisă de instrumente MCP, politica de jurnalizare și aprobatorul scrierii.

Rulați o clonare doar în citire, o citire de metadate REST și o citire de instrument MCP cu substituenți în transcriere. Comparați rezultatele. Păstrați profilul agentului doar în citire până când registrul și jurnalele trec de verificare.

Când apare o sarcină de scriere, pregătiți mai întâi un diff local. Prezentați ramura țintă, căile modificate, metoda API cerută, scopul tokenului și pasul de revenire. Folosiți o identitate separată de scriere, cu durată scurtă, numai după ce o persoană aprobă acțiunea exactă.
