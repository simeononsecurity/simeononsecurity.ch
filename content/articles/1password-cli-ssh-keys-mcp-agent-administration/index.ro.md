---
title: "1Password SSH Agent and CLI: Acces în mod de doar citire pentru agenți AI"
date: 2026-10-11
lastmod: 2026-10-28
toc: true
draft: false
description: "Proiectați un flux de lucru SSH în mod de doar citire cu 1Password CLI, SSH Agent și MCP. Folosiți comenzi sintetice, permisiuni restrânse și aprobare umană înainte de testarea în mediu real."
genre: ["Administrare de sistem", "Securitate în cloud", "Automatizare"]
tags: ["1Password CLI", "chei SSH", "1Password SSH Agent", "MCP", "Model Context Protocol", "administrare de agenți", "administrare de sisteme", "Bitbucket Cloud", "Git prin SSH", "referințe la secrete", "conturi de serviciu", "privilegii minime", "autentificare cu cheie publică", "gestionarea secretelor", "securitate linie de comandă", "siguranță automatizării"]
cover: "/img/cover/1password-cli-ssh-keys-mcp-agent-administration.webp"
coverAlt: "Diagramă abstractă a unui agent care utilizează o referință la un secret, un agent SSH și instrumente MCP, fără a afișa chei private."
coverCaption: ""
---

**Un agent de linie de comandă are nevoie de acces util, nu de o copie a tuturor credențialelor.** Acest ghid prezintă un design delimitat pentru 1Password CLI, Agentul SSH 1Password, accesul Git Bitbucket și Protocolul de Context al Modelului (MCP). Primul flux de lucru utilizează nume sintetice, acțiuni doar de citire și aprobare umană la granița SSH.

<!--more-->

Distincția cheie este simplă. **SSH interactiv utilizează consimțământul prin Agentul SSH 1Password. Automatizarea neasistată necesită o identitate separată, un acces restrâns și un ciclu de viață diferit al cheii.** Nu tratați o conexiune MCP ca pe o permisiune de a rula oricare dintre fluxurile de lucru.

## Puncte cheie

- **Protecția cheii private:** Agentul SSH 1Password efectuează autentificarea SSH, păstrând cheile private în aplicația 1Password.
- **Gestionarea cheii publice:** Publicați doar o cheie publică către Bitbucket sau un cont remote. Păstrați jumătatea privată într-un element SSH Key.
- **Consimțământ interactiv:** O persoană aprobă un client sau o sesiune de terminal înainte ca Agentul SSH să utilizeze o cheie.
- **Separare pentru neasistență:** Un job programat necesită un cont de serviciu dedicat și un domeniu de vault restrâns. O aprobare a Agentului SSH interactiv nu satisface această necesitate.
- **Granițe MCP:** MCP conectează un agent la instrumente și resurse. Clientul, serverul, sistemul de operare și politica 1Password controlează în continuare accesul.

## Înainte de a începe

**Prerechizite:** Instalați 1Password 8 și 1Password CLI 2.20.0 sau o versiune ulterioară. Autentificați-vă printr-un cont 1Password suportat. Utilizați un client OpenSSH. Creați un depozit de test Bitbucket sau altă țintă non-producție. Păstrați o cale administrativă secundară disponibilă pentru revenire.

**Timp:** 30 la 45 de minute pentru o revizuire a designului și o parcurgere sintetică.

**Dificultate:** Intermediar. Aveți nevoie de cunoștințe de bază despre Git, SSH, shell și controlul accesului.

Acest ghid acoperă designul și planificarea. Articolul Bitbucket legat acoperă granițele de acces specifice Bitbucket. Acest ghid nu testează un cont live, nu creează o cheie reală, nu se conectează la un gazdă real și nu înregistrează un server MCP real. Fiecare identificator de mai jos este sintetic. **Înlocuiți placeholder-urile doar în cadrul propriului mediu controlat.**

**Poziție de versiune:** Utilizați 1Password 8 și [1Password CLI 2.20.0 sau o versiune ulterioară](https://www.1password.dev/ssh/manage-keys) pentru acest flux de lucru. [1Password CLI 1 este depreciat](https://www.1password.dev/cli/upgrade/). [1Password 7 se retrage la începutul anului 2027](https://support.1password.com/add-account/). Generarea, importul și partajarea cheilor SSH necesită 1Password 8. Confirmați versiunile Git, OpenSSH, gazdei MCP și serverului MCP instalate înainte de testare. Exemplele de mai jos rămân netestate.

Un **vault** este o colecție protejată de elemente din 1Password. **OpenSSH** este software-ul de client și server SSH utilizat de multe sisteme de operare. **MCP**, sau Model Context Protocol, conectează un agent la instrumente sau resurse aprobate.

## De ce să păstrezi cheile private necitite

O pereche de chei SSH are o cheie publică și o cheie privată. Un serviciu Git sau un server remote stochează cheia publică. Clientul demonstrează deținerea cheii private în timpul autentificării. Cheia privată nu trebuie să ajungă la serviciul remote.

[1Password SSH Agent](https://www.1password.dev/ssh/agent) extinde acest model. Documentația sa menționează că clienții SSH și Git se autentifică prin agent, în timp ce cheia privată rămâne în aplicația 1Password. Clientul primește un rezultat de semnare, nu un fișier de cheie privată.

Această limită reduce mai multe căi de expunere:

- **Controlul surselor:** O cheie privată nu intră într-un depozit sau într-o cerere de extracție (pull request).
- **Istoricul shell-ului:** O valoare de cheie privată nu apare într-un argument de comandă.
- **Fișiere temporare:** Un script nu trebuie să scrie o cheie privată în `~/.ssh/`.
- **Contextul agentului:** Un model de limbaj mare (LLM) nu are nevoie de textul cheii private pentru a solicita o operație SSH.
- **Reutilizare accidentală:** O cheie copiată nu rămâne într-un spațiu de lucru vechi după terminarea unei sarcini.

Limita nu face SSH inofensiv. Un proces cu permisiunea de a utiliza soclul agentului ar putea efectua acțiuni în numele cheii aprobate. Verificarea cheii gazdei, limitările conturilor remote, permisiunile depozitului, politica comenzilor și izolarea proceselor rămân importante.

*Limita cheii private protejează materialul cheii. Limita nu aprobă o comandă remote sau nu dovedește că gazda țintă este de încredere.*

## Consimțământul SSH interactiv

Configurează un vault dedicat pentru cheile agentului. Folosește fișierul de configurare SSH Agent pentru a selecta cel mai mic set de chei și o cheie specifică gazdei. Nu expune fiecare cheie eligibilă din fiecare vault integrat unui proces de automatizare.

[Modelul de securitate 1Password SSH Agent](https://www.1password.dev/ssh/agent/security) leagă aprobarea de o cheie și de un proces solicitant. Prompt-ul identifică procesul și cheia. Persoana aprobă apoi cererea prin metoda de autentificare configurată.

1Password documentează mai multe domenii de aprobare. Aprobarea per-cheie și per-aplicație este implicită. Un domeniu de sesiune de terminal restrânge aprobarea la un tab sau o sesiune. Aprobarea per-cerere întreabă din nou pentru fiecare cerere. O opțiune de aprobare pentru toate procesele există, dar această opțiune oferă tuturor proceselor din sub utilizatorul curent al sistemului de operare acces pentru sesiune.

**Utilizați cea mai îngustă gamă de aprobare potrivită pentru sarcină.** Un agent de administrare a sistemelor ar trebui să ruleze într-un terminal dedicat sau într-un mediu izolat (sandbox). Nu aprobați fiecare proces atunci când o singură sesiune de terminal este suficientă.

Sesiunea de aprobare nu este o acordare permanentă. 1Password înregistrează autorizarea pentru perioada configurată sau până când aplicația se blochează sau se închide. Când aplicația este blocată, agentul nu reține cheile private pentru utilizare ulterioară. Procesul SSH Agent continuă în fundal atunci când setarea suportată este activată, în timp ce 1Password este închis, dar o nouă cerere de semnare necesită deblocarea 1Password.

[ghidul de configurare SSH 1Password](https://www.1password.dev/ssh/get-started) prezintă fluxul general: generați sau importați o cheie, publicați cheia publică, activați SSH Agent, configurați clientul SSH, rulați o comandă SSH sau Git și aprobați cererea. Calea exactă a soclului (socket) diferă în funcție de sistemul de operare. Folosiți instrucțiunile pentru platforma curentă în loc să copiați o cale de pe altă mașină.

Aplicația 1Password trebuie să fie deblocată înainte ca o nouă cerere de semnare să aibă succes. Procesul agentului poate continua în fundal în timp ce aplicația este închisă. O aplicație blocată nu eliberează materialul cheii private pentru semnare.

## Chei publice și Bitbucket

[ghidul de gestionare a cheilor 1Password](https://www.1password.dev/ssh/manage-keys) documentează elementele SSH Key, generarea cheilor, importul cheilor, cheile publice, amprentele și cheile private. Exemplul CLI utilizează `op item create --category ssh` pentru a crea un element SSH Key. 1Password CLI generează implicit o cheie Ed25519 pentru acest exemplu și ascunde cheia privată în ieșirea sa.

Bitbucket Cloud utilizează fluxul de lucru normal de linie de comandă Git și OpenSSH. [ghidul său de linie de comandă](https://support.atlassian.com/bitbucket-cloud/docs/find-the-command-line/) descrie operațiile Git dintr-un depozit local. [ghidul său de configurare SSH](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) enumeră formele remote SSH și formatele de chei publice acceptate.

**Tratați Bitbucket ca pe un consumator de chei publice.** Înregistrați cheia publică sau amprenta prin contul Bitbucket aprobat sau prin setarea depozitului. Păstrați cheia privată în 1Password. Clientul Git solicită agentului SSH să semneze. Clientul nu citește un fișier de cheie privată.

Pentru domeniul cheii de acces Bitbucket, calea de înregistrare și testul Git doar-citire, consultați [Bitbucket Cloud SSH Keys and Git CLI: Read-Only Access for AI Agents](/articles/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation/).

Documentația Bitbucket numește acest lucru flux de lucru Git CLI. Acest articol nu presupune un server MCP separat Bitbucket sau un produs numit Bitbucket CLI. Un CLI specific Bitbucket necesită propria sa documentație curentă și propria sa revizuire a permisiunilor.

## Granița dintre Agent și MCP

Utilizați specificația curentă [MCP](https://modelcontextprotocol.io/specification/2026-07-28) atunci când evaluați un server nou.

URL-ul specificației din 2025-06-18 din paragraful de context de mai jos este o versiune istorică. Utilizați specificația din 2026-07-28 pentru evaluările noi.

[Standardul MCP](https://modelcontextprotocol.io/specification/2025-06-18) standardizează conexiunile dintre o aplicație LLM, un conector client și un server. Un server oferă instrumente, resurse sau prompturi. Specificația precizează, de asemenea, că gazdele trebuie să obțină consimțământul utilizatorului înainte de a expune date sau de a invoca instrumente.

**MCP în sine nu acordă permisiuni.** Un instrument MCP rulează în continuare în cadrul permisiunilor procesului serverului, al utilizatorului sistemului de operare, al căii de rețea, al contului de cloud și al credențialelor configurate. O descriere a instrumentului nu este o politică de autorizare.

[Documentația 1Password Security for AI](https://www.1password.dev/security-for-ai) descrie un server MCP Environments și modele de configurare securizată MCP. Aceeași pagină descrie încărcarea în timpul execuției a valorilor de configurare MCP din 1Password. Aceste pagini nu definesc un produs generic MCP pentru chei SSH 1Password sau un flux de lucru universal SSH pentru fiecare client agent.

Utilizați MCP ca o suprafață de control restrânsă:

- **Instrumente de citire:** Inspecționați starea serviciului, metadatele depozitului sau jurnalele aprobate.
- **Instrumente de planificare:** Pregătiți o comandă sau un registru de modificări fără a executa comanda.
- **Instrumente de aprobare:** Solicitați o decizie umană înainte de o scriere la distanță.
- **Instrumente de scriere:** Păstrați-le dezactivate până când ținta, comanda, domeniul de aplicare și planul de revenire la starea anterioară sunt explicite.

Agentul ar trebui să primească referințe, metadate și rezultate de operațiune. **Agentul nu ar trebui să primească textul cheii private, un descărcare completă a elementelor din vault sau un shell nelimitat.**

## O politică sigură inițială

Începeți cu o politică scrisă înainte de a activa un agent. Păstrați politica aproape de configurația MCP, dar nu plasați credențiale în fișier.

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

Această politică este un exemplu, nu un format de configurare 1Password. Stocați politica reală în planul de control utilizat de clientul agentului dvs. Revizuiți fiecare instrument în raport cu politica înainte de a activa fiecare instrument.

## Conturi de serviciu și referințe la secrete

Un **cont de serviciu** oferă unui proces automatizat propria identitate. [Ghidul de scripturi CLI 1Password](https://www.1password.dev/cli/secrets-scripts) recomandă conturile de serviciu pentru accesul cu privilegii minime la vault-uri selectate. Acest lucru separă un job neasistat de SSO, MFA, inventarul vault și contul zilnic al unei persoane.

O **referință secretă** numește o valoare fără a plasa valoarea în sursă. [Referința CLI 1Password](https://www.1password.dev/cli/reference) utilizează forma `op://vault/item/field`. Referința este sigură de stocat doar atunci când procesul înconjurător are încă un acces restrâns. O referință nu ocolește politica.

Folosiți `op read` atunci când o comandă are nevoie de o singură valoare. Folosiți `op run` atunci când un proces copil are nevoie de un set controlat de valori de execuție. Folosiți `op item create` atunci când un nou element SSH Key trebuie să existe în coiful aprobat.

Nu confundați injectarea la execuție cu protecția cheii private. Un token API transmis ca variabilă de mediu este tot vizibil pentru procesul copil. O cheie privată transmisă printr-o variabilă de mediu este și mai gravă, deoarece valoarea extinde expunerea către inspecția procesului, rapoartele de eroare, ieșirea de depanare, urmărirea shell-ului și înregistrarea accidentală.

**Preferă o referință în sursă și o valoare de execuție în cel mai mic proces posibil.** Păstrați procesul de scurtă durată. Dezactivați urmărirea shell-ului. Nu afișați mediul. Eliminați fișierele temporare după o execuție eșuată.

## Flux de lucru sigur inițial

Secvența de mai jos separă înregistrarea cheii publice, SSH interactiv, descoperirea MCP și designul neasistat.

### 1. Definiți ținta

Scrieți clasa țintă, contul remote, depozitul sau comanda intenționată, sursa cheii de gazdă, proprietarul aprobării și acțiunea de revenire. Folosiți un înregistrare sintetică în timpul primei exerciții.

```text
target_class: test-repository
remote_account: git
operation: read-only connectivity check
host_key_source: approved administrator record
approval_owner: named operator
rollback: remove public key and revoke test identity
```

**Rezultat așteptat, netestat:** Înregistrarea identifică o singură țintă și o singură operațiune. Înregistrarea nu conține un nume de gazdă, o adresă IP, un token, o cheie privată sau date personale.

### 2. Creați sau selectați elementul SSH Key

Ghidul oficial [1SSH key guide](https://www.1password.dev/ssh/manage-keys) documentează modelul de creare CLI. Comanda de mai jos utilizează un titlu sintetic și un coiful de test numit.

```bash
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
```

**Ieșire așteptată, netestată:** 1Password creează un element SSH Key în coiful de test numit și maschează cheia privată în ieșirea terminalului. Comanda modifică starea 1Password. Ieșirea exactă lizibilă de om depinde de versiunea CLI și de starea de autentificare.

Capturați identificatorul de element returnat în înregistrarea de test, fără a copia câmpul cheii private. Folosiți identificatorul sau titlul exact al elementului pentru citiri ulterioare specifice câmpului, doar după ce schema elementului este confirmată.

Nu redirecționați această ieșire către un jurnal partajat. Capturați doar identificatorul de element, amprenta cheii publice și înregistrarea de aprobare, atunci când procedura locală suportă o ieșire structurată sigură.

### 3. Gestionați cheia publică

Deschideți elementul Cheie SSH în 1Password și folosiți acțiunea Copiere cheie publică. Folosiți o referință specifică câmpului doar după ce confirmați eticheta câmpului cheie publică în contul dumneavoastră. Nu exportați elementul complet.

```bash
PUBLIC_KEY_REF="op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
op read "$PUBLIC_KEY_REF"
```

**Rezultat așteptat, netestat:** O linie sintetică de cheie publică OpenSSH sau o valoare de cheie publică din câmpul confirmat. Numele câmpului placeholder de mai sus nu este o garanție privind eticheta câmpului din elementul dumneavoastră.

Înregistrați cheia publică în contul Bitbucket aprobat, în depozitul Bitbucket sau în contul remote. Nu lipiți niciodată cheia privată corespunzătoare în Bitbucket. Ghidul SSH Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification) recomandă, de asemenea, înregistrarea cheii de gazdă Bitbucket înainte de prima conexiune.

Pentru Bitbucket, preluați înregistrarea cheii de gazdă publicate și comparați înregistrarea cu o copie de încredere independentă înainte de a adăuga o linie în `~/.ssh/known_hosts`. Folosiți verificarea strictă a gazdei după ce comparația reușește. Nu acceptați o cheie de gazdă modificată în timpul unei execuții de agent.

### 4. Activare SSH interactiv

Activați Agentul SSH 1Password în aplicația desktop. Configurați OpenSSH cu valoarea specifică platformei `IdentityAgent` sau `SSH_AUTH_SOCK` din ghidul oficial de configurare](https://www.1password.dev/ssh/get-started). Limitați primul test la un singur depozit sau la un singur cont non-producție.

Pe macOS sau Linux, setați soclul din ghidul de configurare al platformei și rulați `ssh-add -l`. Pe Windows, folosiți configurația de tub numit (named-pipe) acceptată și verificați cheile disponibile prin interfața Agentului SSH 1Password sau printr-un test SSH Windows documentat. Nu prezentați `ssh-add -l` ca o comandă de verificare cross-platform.

Doar pe macOS sau Linux:

```bash
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Rezultat așteptat, netestat:** Pe macOS sau Linux, `ssh-add -l` listează amprentele din agentul activ. Pe Windows, folosiți testul de tub numit documentat sau interfața Agentului SSH 1Password. O citire Git reușită returnează o referință de commit. Placeholder-ul de depozit de mai sus necesită înlocuire într-un test controlat.

Comanda folosește un placeholder de depozit. Înlocuiți placeholder-ul doar într-un test controlat. **Nu aprobați un prompt pentru o țintă sau un proces pe care nu l-ați așteptat.**

### 5. Adăugare MCP după ce calea SSH funcționează

Verificați mai întâi clientul SSH și ținta fără MCP. Apoi adăugați un singur server MCP sau conector local doar pentru citire. Furnizați agentului un instrument precum `read_status` sau `prepare_command`. Nu începeți cu un instrument de shell general.

Configurația MCP ar trebui să facă referire la valorile de runtime prin mecanismul de mediu suportat de client. [Ghidul de securitate AI 1Password](https://www.1password.dev/security-for-ai) descrie înlocuirea token-urilor de configurare MCP în text clar cu variabile de mediu încărcate din 1Password. **Păstrați referința sau numele variabilei în configurație. Păstrați valoarea rezolvată în afara transcripției agentului.**

Această secțiune descrie un design, nu o configurare MCP testată. Niciun client, server, transport, versiune sau fixture nu este fixat aici. Validați un server read-only într-un profil de test separat înainte de a conecta un agent la un sistem de producție.

### 6. Înregistrați rezultatul

Înregistrați clasa țintă, numele instrumentului, decizia de aprobare, amprenta cheii publice, rezultatul comenzii și rezultatul curățării. Omiteti valorile secrete. Marcați fiecare ieșire ca observată sau așteptată.

**Rezultat așteptat, netestat:** Agentul citește starea, propune o comandă limitată, primește aprobare explicită pentru cererea SSH, completează operațiunea read-only și produce un registru fără textul cheii private.

## Secvență de comenzi sintetică

Următoarea secvență arată ordinea fără a utiliza infrastructură reală. Aceste comenzi sunt doar exemple. Nu au fost executate în timpul pregătirii articolului.

```bash
op --version
op item create --category ssh --ssh-generate-key=ed25519 --vault "synthetic-test-vault" --title "synthetic-agent-admin-key"
op read "op://synthetic-test-vault/synthetic-agent-admin-key/synthetic-public-key-field"
# macOS or Linux only
ssh-add -l
git ls-remote "<repository-ssh-url>" HEAD
```

**Ieșire așteptată, netestată:**

```text
2.x.y
SSH Key item created. Private key: redacted
ssh-ed25519 AAAA<synthetic-public-key> synthetic-key-label
256 SHA256:<synthetic-fingerprint> synthetic-agent-admin-key (ED25519)
<synthetic-commit-id>        HEAD
```

Blocul de ieșire este ilustrativ. Blocul nu reprezintă o execuție împotriva unui cont 1Password, Bitbucket, unui furnizor Git sau a unui gazdă remote. Un registru de producție ar trebui să stocheze doar metadate aprobate și o stare de succes sau eșec.

## Acces interactiv versus neasistat

| Mod de acces | Identitate | Calea cheii private | Model de aprobare |
|---|---|---|---|
| **SSH interactiv** | Cont uman prin 1Password SSH Agent | Cheia privată rămâne în aplicația 1Password | Oamenii aprobă un proces, o sesiune de terminal sau o cerere |
| **Citire programată** | Cont de serviciu dedicat | `op run` furnizează valori de runtime restrânse | Politica job-ului și domeniul contului de serviciu |
| **SSH programat** | Identitate de automatizare dedicată | Exportul cheii rămâne un design de ultimă instanță | Izolarea job-ului, durată scurtă, restricția gazdei și rotația |
| **Scriere agent** | Identitate umană sau specifică sarcinii | Depinde de integrarea aprobată | Aprobare umană înainte de fiecare modificare definită |

*Nu programați un flux de lucru în jurul unui prompt de agent SSH interactiv. Folosiți un design de automatizare separat sau păstrați pasul operat de un om.*

Pentru joburile neasistate, creați un cont de serviciu cu acces la un singur vault sau la un set mic de elemente. Acordați jobului un singur scop. Folosiți un depozit dedicat sau un cont de server dedicat. Adăugați verificarea cheii gazdă. Stabiliți un timeout de execuție. Înregistrați metadatele acțiunilor fără secrete. Rotați sau revocați identitatea după test.

Dacă un job neasistat are cu adevărat nevoie de o cheie SSH privată, folosiți o cheie de automatizare dedicată, cu un cont remote îngust și o dată de expirare documentată. Obținerea cheii private cu `op read` exportă totuși materialul cheii peste o graniță de proces. Acest design are un impact mai mare decât 1Password SSH Agent. Preferați o identitate de platformă, un serviciu de deploy sau o altă identitate de sarcină de lucru atunci când ținta suportă una dintre acestea.

## De ce variabilele de mediu în text simplu cresc riscul

Variabilele de mediu țin secretele în afara fișierelor sursă, dar nu le fac invizibile. Un proces fiu își citește mediul. Inspectarea proceselor, gestionarii de erori, ieșirile de depanare, urmărirea shell-ului și înregistrările de comenzi copiate pot expune valorile.

1Password documentează `op run` ca metodă de runtime pentru încărcarea referințelor într-un subproces. Folosiți `op run` pentru valorile de care un proces are cu adevărat nevoie. Păstrați procesul fiu cu viață scurtă și restricționați comanda sa. Nu transmiteți o cheie privată prin `SSH_PRIVATE_KEY`, `KEY` sau o variabilă similară atunci când SSH Agent elimină necesitatea exportului.

Ordinea mai sigură este:

1. **Folosiți SSH Agent** pentru SSH interactiv.
2. **Folosiți înregistrarea cheii publice** pentru Bitbucket sau contul remote.
3. **Folosiți `op run`** pentru un proces fiu neasistat cu scop îngust.
4. **Folosiți `op read`** pentru o singură valoare atunci când un proces fiu nu are nevoie de un mediu complet.
5. **Exportați o cheie privată** doar după o excepție scrisă, un domeniu de aplicare îngust, un plan de curățare și un plan de rotație.

## Tabel de decizie

| Necesitate | Cale preferată | Motiv pentru oprire sau redesignare |
|---|---|---|
| Omul rulează Git prin SSH | 1Password SSH Agent | Opriți dacă promptul menționează un proces sau o cheie neașteptată |
| Înregistrarea unei chei de depozit | Citiți sau completați automat cheia publică | Nu copiați niciodată cheia privată în serviciul de depozit |
| Agentul citește starea serviciului | Instrument MCP doar pentru citire cu domeniu la nivel de OS | Opriți dacă instrumentul expune un shell nelimitat |
| Agentul propune o modificare la distanță | Instrument de planificare urmat de aprobare umană | Opriți dacă ținta, comanda sau procedura de revenire la starea anterioară nu sunt clare |
| Job-ul citește un token API | Cont de serviciu plus `op read` sau `op run` | Opriți dacă tokenul intră în sursă, jurnale sau un profil global |
| Job-ul are nevoie de acces SSH | Identitate de sarcină de lucru sau cheie de automatizare dedicată | Opriți dacă job-ul necesită o cheie personală sau un cont larg |
| Configurația MCP are nevoie de un token | Referință de runtime încărcată de clientul suportat | Opriți dacă un token în text clar este commituit în configurație |

## Gestionarea eșecurilor

**Prompt neașteptat de consimțământ SSH:** Refuzați promptul. Verificați numele procesului, sesiunea terminalului, amprenta cheii, ținta depozitului și cheia gazdei. Revizuiți configurația clientului SSH înainte de a reîncerca.

**Lipsa soclului SSH Agent:** Confirmați că aplicația desktop 1Password este instalată printr-o metodă suportată, că SSH Agent este activat și că clientul utilizează soclul specific platformei. Pagina oficială a SSH Agent](https://www.1password.dev/ssh/agent) enumeră cerințele de sistem de operare și link-urile pentru configurarea soclului.

**Autentificarea cu cheie publică eșuează:** Verificați cheia publică selectată, contul de la distanță, permisiunea depozitului, cheia gazdei și configurația SSH. Folosiți o comparație a amprentei publice. Nu rezolvați eroarea exportând o cheie privată nerezonabilă.

**`op read` refuză accesul:** Verificați domeniul seifului contului de serviciu, identificatorul elementului, referința câmpului, starea de autentificare și starea elementului. Reduceți referința la un singur element aprobat. Nu lărgiți acordul seifului ca primă reacție.

**`op run` expune o valoare:** Opriți job-ul. Păstrați doar înregistrarea minimă a incidentului. Eliminați jurnalele copiate și fișierele temporare conform procedurii dumneavoastră de retenție. Rotiți secretul sau cheia afectată. Revizuiți urmărirea shell-ului, inspecția proceselor, rapoartele de eroare și retenția transcripțelor MCP.

**Comportamentul neașteptat al instrumentului MCP:** Tratați ieșirea instrumentului ca pe date nefiabile. Opiți înainte de a executa comenzile sugerate de ieșire. Inspectați sursa serverului, configurația, permisiunile și transportul. Gazda MCP trebuie să obțină consimțământul utilizatorului. Specificația oferă, de asemenea, orientări pentru implementatori privind consimțământul și controlul accesului, dar protocolul nu înlocuiește revizuirea dumneavoastră.

## Rollback și eliminarea

Rollback-ul începe cu eliminarea accesului, nu cu ștergerea fișierelor.

1. **Opiți agentul sau sarcina programată.** Dezactivați intrarea serverului MCP sau deconectați clientul.
2. **Blocați 1Password.** Încheiați sesiunea interactivă de autorizare SSH.
3. **Eliminați cheia publică.** Ștergeți cheia de testare din Bitbucket, din depozit sau din contul remote.
4. **Revocați contul de serviciu.** Eliminați accesul său la vault și invalidați token-ul său.
5. **Ștergeți elementul de cheie SSH de testare** după ce ați confirmat că niciun flux de lucru aprobat nu utilizează acest element.
6. **Eliminați configurația temporară.** Ștergeți referințele de testare, suprascrierile locale ale socket-ului și jurnalele generate.
7. **Revizuiți dovezile.** Confirmați că înregistrarea de rollback nu conține nicio cheie privată, token sau dump de mediu.

*Ștergerea unui fișier local nu revocă o cheie publică, un cont de serviciu, un token în cache sau o autorizare remote. Eliminați fiecare acordare la sursa sa.*

## Depanare

### Agentul solicită o cheie la fiecare comandă

Verificați domeniul de autorizare selectat. Aprobarea per cerere este mai restrictivă. O sesiune de terminal sau de aplicație s-ar fi putut încheia. 1Password solicită, de asemenea, din nou după un eveniment de blocare sau ieșire.

### Agentul vede o cheie privată în transcrierea sa

Opiți fluxul de lucru și rotiți cheia. Inspectați răspunsul serverului MCP, comanda shell, jurnalul de depanare și învelitoarea instrumentului. Înlocuiți citirile cheii private cu utilizarea SSH Agent pentru sarcinile interactive. Pentru job-uri, înlocuiți cheia personală cu o identitate dedicată și o excepție documentată.

### O listă de chei conține prea multe identități

Agentul SSH 1Password expune cheile eligibile din vault-urile sale configurate. Folosiți o configurație de agent cu domeniu limitat sau o configurație SSH specifică gazdei. [Documentația agentului](https://www.1password.dev/ssh/agent) menționează, de asemenea, limita de șase chei a serverului OpenSSH.

### O comandă funcționează manual, dar eșuează într-un job

Comparați identitatea, domeniul vault-ului, mediul, datele cheii gazdei, directorul de lucru și ipotezele de aprobare. O sesiune interactivă 1Password include consimțământul uman. Un job programat nu. Proiectați job-ul ca pe un mod de acces separat.

### Serverul MCP este conectat, dar sarcina eșuează

Conexiunea nu dovedește autorizarea. Verificați descoperirea instrumentelor, credențialele serverului, consimțământul clientului, permisiunile sistemului de operare, accesul la rețea și permisiunile de pe partea țintă, în pași separați. Păstrați primul test doar în mod de citire.

## Pașii următori

Utilizați specificația MCP din 2026-07-28 pentru noi aprobări. Orice link către specificația din 2025-06-18 din acest articol este context istoric.

Începeți cu un singur depozit sintetic și un singur instrument MCP doar de citire. Înregistrați fiecare rezultat așteptat ca netestat, până când un mediu controlat produce dovezi. Apoi repetați fluxul de lucru cu o țintă non-producție, un operator numit, o cheie de gazdă verificată și un registru scris de rollback.

Citiți [referința CLI 1Password](https://www.1password.dev/cli/reference) pentru opțiunile de comandă actuale. Citiți [Încărcarea secretelor în scripturi](https://www.1password.dev/cli/secrets-scripts) înainte de a crea automatizări pentru conturi de serviciu. Citiți [specificația MCP](https://modelcontextprotocol.io/specification/2026-07-28) înainte de a aproba instrumentele de pe un server nou.

**Păstrați SSH interactiv aprobat de un om. Păstrați accesul neasistat separat. Păstrați cheile private necitite ori de câte ori ținta suportă autentificarea bazată pe agent.**
